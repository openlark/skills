#!/usr/bin/env python3
"""
port_skill.py — adapts/ports an OpenClaw skill to another agent platform.

Only performs deterministic mechanical replacement; semantic-level rewriting
(cron logic, cross-session messages, attachment directives) is done manually by
the agent, and the script lists these "needs manual handling" items in its report.

Usage:
    python3 port_skill.py --source <skill-dir> --target <platform> [--out <dir>] [--dry-run]

target values: claude-code | codex | cursor | hermes | opencode | generic

Output layout: <out>/<target>/<skill-name>/...
"""

import argparse
import difflib
import json
import re
import shutil
import sys
from pathlib import Path

TARGETS = ["claude-code", "codex", "cursor", "hermes", "opencode", "generic"]

# OpenClaw tool name -> { target: replacement }. None means no equivalent
# (flagged for manual handling, not replaced).
# Short English words (read/write/edit/exec/process/image/cron) are replaced only inside backticks;
# other non-English words are replaced as word-boundary bare words.
TOOLS = {
    "read": {"claude-code": "Read", "codex": "shell", "cursor": "Read",
             "hermes": "read_file", "opencode": "read", "generic": "read file"},
    "write": {"claude-code": "Write", "codex": "apply_patch", "cursor": "Write",
              "hermes": "write_file", "opencode": "write", "generic": "write file"},
    "edit": {"claude-code": "Edit", "codex": "apply_patch", "cursor": "Edit",
             "hermes": "patch", "opencode": "edit", "generic": "edit file"},
    "exec": {"claude-code": "Bash", "codex": "shell", "cursor": "Run",
             "hermes": "terminal", "opencode": "bash", "generic": "run command"},
    "process": {"claude-code": "Bash", "codex": "shell", "cursor": "Run",
                "hermes": "process", "opencode": "bash", "generic": "run command (background)"},
    "web_fetch": {"claude-code": "WebFetch", "codex": "shell", "cursor": "Web",
                  "hermes": "web_extract", "opencode": "webfetch", "generic": "fetch URL"},
    "image": {"claude-code": "Read", "codex": None, "cursor": None,
              "hermes": "vision_analyze", "opencode": None, "generic": "read image"},
    "cron": {"claude-code": None, "codex": None, "cursor": None,
             "hermes": "cronjob", "opencode": None, "generic": "schedule"},
    "sessions_spawn": {"claude-code": "Task", "codex": "spawn_agent", "cursor": "Subagent",
                       "hermes": "delegate_task", "opencode": None, "generic": "spawn subagent"},
    "sessions_list": {"claude-code": "Task", "codex": None, "cursor": None,
                      "hermes": None, "opencode": None, "generic": "list sessions"},
    "sessions_history": {"claude-code": None, "codex": None, "cursor": None,
                         "hermes": "session_search", "opencode": None, "generic": "session history"},
    "sessions_send": {"claude-code": None, "codex": None, "cursor": None,
                      "hermes": None, "opencode": None, "generic": "cross-session message"},
    "sessions_yield": {"claude-code": None, "codex": None, "cursor": None,
                       "hermes": None, "opencode": None, "generic": "yield turn"},
    "subagents": {"claude-code": "Task", "codex": "spawn_agent", "cursor": "Subagent",
                  "hermes": "delegate_task", "opencode": None, "generic": "manage subagents"},
    "session_status": {"claude-code": None, "codex": None, "cursor": None,
                       "hermes": None, "opencode": None, "generic": "session status"},
    "memory_get": {"claude-code": None, "codex": None, "cursor": None,
                   "hermes": "memory", "opencode": None, "generic": "read memory"},
    "memory_search": {"claude-code": None, "codex": None, "cursor": None,
                      "hermes": "memory", "opencode": None, "generic": "search memory"},
}

# Tools replaced only inside backticks (short English words)
BACKTICK_ONLY = {"read", "write", "edit", "exec", "process", "image", "cron"}

# Plain English words: bare words are not flagged as "no equivalent tool", to avoid
# false positives for og:image / read etc. in prose
PROSE_WORDS = {"read", "write", "edit", "exec", "process", "image"}

# Precompiled regexes (avoids recompiling on every transform_text call)
_BACKTICK_PATTERNS = {tool: re.compile(r"`" + re.escape(tool) + r"`") for tool in TOOLS}
_BARE_PATTERNS = {tool: re.compile(r"\b" + re.escape(tool) + r"\b") for tool in TOOLS}
_AGENTS_PATTERN = re.compile(r"\bAGENTS\.md\b")

# System file reference: AGENTS.md -> CLAUDE.md only for Claude Code
AGENTS_MAP = {"claude-code": "CLAUDE.md"}

# OpenClaw-specific output directives/features, scanned and flagged
FLAG_PATTERNS = {
    "MEDIA:": re.compile(r"MEDIA:"),
    "[embed": re.compile(r"\[embed"),
    "[[reply_": re.compile(r"\[\[reply_(to_current|to:)"),
    "[[audio_as_voice]]": re.compile(r"\[\[audio_as_voice\]\]"),
    "~/.openclaw": re.compile(r"~/.openclaw"),
    "runtime(subagent/acp)": re.compile(r"runtime\s*[:=]\s*[\"']?(subagent|acp)[\"']?"),
    "tbox-ai model alias": re.compile(r"tbox-ai"),
}

TEXT_EXTS = {".md", ".txt"}

# Skill-name markers that depend on OpenClaw platform extensions and are not portable
NON_PORTABLE_MARKERS = ("channel-push", "feishu", "tbox", "redbook", "weavefox", "tboxbook")

# Suspected "tool mapping / tool documentation" filename/title markers (these files
# should be rewritten wholesale, not run through replacement)
TOOL_CATALOG_NAME_MARKERS = ("platform-tool", "tool-map", "toolmap", "tool-reference", "tools-reference", "toolmapping")
TOOL_CATALOG_HEADING_MARKERS = ("tool map", "tool mapping", "platform tool", "tool reference")


def _is_non_portable(skill_name):
    low = skill_name.lower()
    return any(m in low for m in NON_PORTABLE_MARKERS)


def _is_tool_catalog(relname, text):
    """Determine whether an md file documents tool mappings (rather than instructing the agent to use tools)."""
    low = relname.lower()
    if any(m in low for m in TOOL_CATALOG_NAME_MARKERS):
        return True
    for line in text.splitlines()[:60]:
        s = line.strip()
        if s.startswith("#"):
            sl = s.lower()
            if any(m in sl for m in TOOL_CATALOG_HEADING_MARKERS):
                return True
    return False


# Agent Skills spec name constraint: ^[a-z0-9]+(-[a-z0-9]+)*$, 1-64 characters
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def _extract_field(text, key):
    """Extract a single-line or folded/block-scalar key value from frontmatter; returns a string or None."""
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    end = None
    for i in range(1, len(lines)):
        if lines[i].rstrip() in ("---", "..."):
            end = i
            break
    if end is None:
        return None
    fm = lines[1:end]
    for idx, ln in enumerate(fm):
        m = re.match(rf"^{re.escape(key)}\s*:\s*(.*)$", ln)
        if not m:
            continue
        val = m.group(1).strip()
        if val in ("", ">", ">-", ">+", "|", "|-", "|+", "|2", ">2"):
            parts = []
            for ln2 in fm[idx + 1:]:
                if ln2.strip() == "":
                    parts.append("")
                    continue
                if not ln2[0].isspace():
                    break
                parts.append(ln2.strip())
            joined = " ".join(p for p in parts if p)
            return joined if joined else val
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        return val
    return None


def _fix_name(text, new_name):
    """Rewrite the frontmatter name field to new_name."""
    if not text.startswith("---"):
        return text
    return re.sub(r"(?m)^name\s*:.*$", f"name: {new_name}", text, count=1)


# OpenClaw output-directive line patterns (used by --strip-output-directives)
_STRIP_DIRECTIVE_PATTERNS = [
    re.compile(r"MEDIA:"),
    re.compile(r"\[embed"),
    re.compile(r"\[\[reply_to_current\]\]"),
    re.compile(r"\[\[reply_to:"),
    re.compile(r"\[\[audio_as_voice\]\]"),
]

# Names of the output-directive flags in FLAG_PATTERNS (corresponding to _STRIP_DIRECTIVE_PATTERNS above)
OUTPUT_DIRECTIVE_NAMES = ("MEDIA:", "[embed", "[[reply_", "[[audio_as_voice]]")


def _is_output_directive_flag(flag):
    """Determine whether a flag belongs to the output-directive class (already auto-handled by --strip-output-directives)."""
    return any(f"[{name}]" in flag for name in OUTPUT_DIRECTIVE_NAMES)


def _strip_output_directives(text):
    """Delete OpenClaw output-directive lines (MEDIA:/[embed/[[reply_*/[[audio_as_voice]]).
    Returns (cleaned_text, removed_count).

    Skips the frontmatter region (--- ... --- / ...) to avoid mistakenly deleting
    content in fields such as description that merely mention these directive terms
    (e.g. this skill itself explains them in its description).
    """
    lines = text.splitlines(keepends=True)
    # Find the frontmatter boundary: when the file starts with ---, find the closing ---/... index
    fm_end = -1
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() in ("---", "..."):
                fm_end = i
                break
    out_lines = []
    removed = 0
    for idx, line in enumerate(lines):
        if idx <= fm_end:
            out_lines.append(line)  # keep frontmatter (including boundaries) as-is
            continue
        content = line.strip()
        if any(p.search(content) for p in _STRIP_DIRECTIVE_PATTERNS):
            removed += 1
        else:
            out_lines.append(line)
    return "".join(out_lines), removed


def validate_skill(skill_dir):
    """Validate a skill directory against the Agent Skills spec; returns a list of problems (empty = pass)."""
    skill_dir = Path(skill_dir)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["SKILL.md not found"]
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    problems = []
    if not text.startswith("---"):
        problems.append("missing YAML frontmatter (does not start with ---)")
        return problems

    name = _extract_field(text, "name")
    desc = _extract_field(text, "description")
    dir_name = skill_dir.name

    if name is None:
        problems.append("frontmatter missing name field")
    else:
        if len(name) > 64:
            problems.append(f"name exceeds 64 characters: {name}")
        elif not NAME_RE.match(name):
            problems.append(f"name invalid (must match ^[a-z0-9]+(-[a-z0-9]+)*$): {name}")
        elif name != dir_name:
            problems.append(f"name ({name}) does not match directory name ({dir_name})")

    if desc is None or desc.strip() == "":
        problems.append("frontmatter missing non-empty description")
    elif len(desc) > 1024:
        problems.append(f"description exceeds 1024 characters (currently {len(desc)})")

    return problems


def transform_text(text, target, flags, relpath):
    """Apply replacements to the content of a single text file; returns (new_text, change_count)."""
    changes = 0

    # 1) backticked tool-name replacement (all tools)
    for tool, tmap in TOOLS.items():
        repl = tmap.get(target)
        if repl is None:
            continue
        pat = _BACKTICK_PATTERNS[tool]
        n = len(pat.findall(text))
        if n:
            text = pat.sub(f"`{repl}`", text)
            changes += n

    # 2) bare-word replacement (non-English-word tools only)
    for tool, tmap in TOOLS.items():
        if tool in BACKTICK_ONLY:
            continue
        repl = tmap.get(target)
        if repl is None:
            continue
        pat = _BARE_PATTERNS[tool]
        n = len(pat.findall(text))
        if n:
            text = pat.sub(repl, text)
            changes += n

    # 3) system file reference replacement
    if target in AGENTS_MAP:
        repl = AGENTS_MAP[target]
        pat = _AGENTS_PATTERN
        n = len(pat.findall(text))
        if n:
            text = pat.sub(repl, text)
            changes += n

    # 4) flag items needing manual handling (not replaced)
    for line_no, line in enumerate(text.splitlines(), 1):
        for name, pat in FLAG_PATTERNS.items():
            if pat.search(line):
                flags.append(f"{relpath}:{line_no}: [{name}] {line.strip()}")
        # Flag tools with no equivalent (backticked always flagged; bare words only for non-English prose words)
        for tool, tmap in TOOLS.items():
            repl = tmap.get(target)
            if repl is not None:
                continue
            if _BACKTICK_PATTERNS[tool].search(line):
                flags.append(f"{relpath}:{line_no}: [no equivalent tool {tool}] {line.strip()}")
            elif tool not in PROSE_WORDS and _BARE_PATTERNS[tool].search(line):
                flags.append(f"{relpath}:{line_no}: [no equivalent tool {tool}] {line.strip()}")

    return text, changes


def normalize_frontmatter(text, target):
    """Normalize frontmatter: remove allowed-tools for non-claude-code targets."""
    if target == "claude-code":
        return text
    if not text.startswith("---"):
        return text
    lines = text.splitlines()
    # Find the closing --- / ... (only match column-0 delimiters, to avoid misjudging an
    # indented --- inside a folded description)
    end = None
    for i in range(1, len(lines)):
        if lines[i].rstrip() in ("---", "..."):
            end = i
            break
    if end is None:
        return text
    fm = lines[1:end]
    out = []
    skipping = False
    for ln in fm:
        if re.match(r"^allowed-tools\s*:", ln):
            skipping = True
            continue
        if skipping:
            if ln.strip() == "" or (ln and not ln[0].isspace()):
                skipping = False
            else:
                continue
        out.append(ln)
    return "\n".join(lines[:1] + out + lines[end:])


def port_skill(src, target, out, dry_run=False, fix_name=False, strip_output_directives=False):
    """Port a single OpenClaw skill, returning a result dict (testable).

    Return keys: src, target, skill_name, dst_root, files_copied, files_changed,
                 total_changes, flags, warnings, non_portable, diffs, directives_removed
    """
    src = Path(src).resolve()
    if not src.is_dir():
        raise ValueError(f"source not a directory: {src}")
    if not (src / "SKILL.md").exists():
        raise ValueError(f"SKILL.md not found in {src}")
    if target not in TARGETS:
        raise ValueError(f"unknown target: {target}")

    skill_name = src.name
    dst_root = Path(out).resolve() / target / skill_name

    warnings = []
    non_portable = _is_non_portable(skill_name)
    if non_portable:
        warnings.append(f"Not portable: skill {skill_name} depends on OpenClaw platform extensions (channel-push/feishu/tbox/redbook, etc.); recommend skipping the whole skill.")

    src_name = _extract_field((src / "SKILL.md").read_text(encoding="utf-8", errors="replace"), "name")
    name_mismatch = src_name is not None and src_name != skill_name
    if name_mismatch:
        if fix_name:
            warnings.append(f"name ({src_name}) does not match directory name ({skill_name}); fixed automatically via --fix-name to {skill_name}.")
        else:
            warnings.append(f"name ({src_name}) does not match directory name ({skill_name}) — strict platforms (opencode/Agent Skills validation) will reject it. Use --fix-name to fix automatically.")

    if not dry_run:
        if dst_root.exists():
            shutil.rmtree(dst_root)
        dst_root.mkdir(parents=True, exist_ok=True)

    flags = []
    diffs = []
    files_copied = 0
    files_changed = 0
    total_changes = 0
    directives_removed = 0

    for p in sorted(src.rglob("*")):
        if p.is_dir():
            continue
        rel = p.relative_to(src)
        is_text = p.suffix.lower() in TEXT_EXTS
        if is_text:
            orig = p.read_text(encoding="utf-8", errors="replace")
            if _is_tool_catalog(str(rel), orig):
                warnings.append(f"Tool mapping document: {rel} skipped auto-replacement; must be fully rewritten as the target platform's tool table.")
                files_copied += 1
                if not dry_run:
                    dst = dst_root / rel
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    dst.write_text(orig, encoding="utf-8")
                continue
            text = orig
            if rel.name == "SKILL.md":
                if fix_name and name_mismatch:
                    text = _fix_name(text, skill_name)
                text = normalize_frontmatter(text, target)
            file_flags = []
            text, n = transform_text(text, target, file_flags, str(rel))
            files_copied += 1
            if n:
                files_changed += 1
                total_changes += n
            if strip_output_directives:
                text_after_strip, n_strip = _strip_output_directives(text)
                if n_strip:
                    # Output directives already auto-removed are no longer flagged as "needs manual handling"
                    file_flags = [f for f in file_flags if not _is_output_directive_flag(f)]
                    file_flags.append(f"{rel}: (auto-removed {n_strip} output directive(s))")
                directives_removed += n_strip
                text = text_after_strip
            flags.extend(file_flags)
            if text != orig:
                diffs.append((str(rel), orig, text))
            if not dry_run:
                dst = dst_root / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(text, encoding="utf-8")
        else:
            files_copied += 1
            if not dry_run:
                dst = dst_root / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, dst)

    return {
        "src": str(src),
        "target": target,
        "skill_name": skill_name,
        "dst_root": str(dst_root),
        "files_copied": files_copied,
        "files_changed": files_changed,
        "total_changes": total_changes,
        "flags": flags,
        "warnings": warnings,
        "non_portable": non_portable,
        "diffs": diffs,
        "directives_removed": directives_removed,
    }


def port_skill_all(src, out, dry_run=False, fix_name=False, strip_output_directives=False):
    """Batch-port to all target platforms, returning {target: result}."""
    results = {}
    for t in TARGETS:
        results[t] = port_skill(src, t, out, dry_run=dry_run, fix_name=fix_name,
                                strip_output_directives=strip_output_directives)
    return results


def _dedup(items):
    seen = set()
    out = []
    for x in items:
        if x in seen:
            continue
        seen.add(x)
        out.append(x)
    return out


def _print_report(r, dry_run):
    """Print the report for a single port result, returning the deduplicated flags."""
    print(f"source : {r['src']}")
    print(f"target : {r['target']}{'  (dry-run)' if dry_run else ''}")
    print(f"output : {r['dst_root']}")
    print(f"files  : {r['files_copied']} copied, {r['files_changed']} changed ({r['total_changes']} substitutions)")
    if r["directives_removed"]:
        print(f"stripped: {r['directives_removed']} output directive lines removed")

    print()
    if r["warnings"]:
        print(f"=== Warnings ({len(r['warnings'])}) ===")
        for w in r["warnings"]:
            print("  " + w)
        print()
    if dry_run and r["diffs"]:
        print(f"=== Change preview ({len(r['diffs'])} file(s)) ===")
        for rel, old, new in r["diffs"]:
            print(f"--- {rel}")
            diff = difflib.unified_diff(old.splitlines(), new.splitlines(), fromfile=rel, tofile=rel, lineterm="")
            for line in diff:
                print("  " + line)
        print()
    flags = _dedup(r["flags"])
    if flags:
        print(f"=== Needs manual handling ({len(flags)} item(s)) ===")
        for f in flags:
            print("  " + f)
    else:
        print("No items need manual handling.")
    return flags


def main():
    ap = argparse.ArgumentParser(description="Port an OpenClaw skill to another agent platform.")
    ap.add_argument("--source", required=True, help="Path to the OpenClaw skill directory.")
    ap.add_argument("--target", required=True, choices=TARGETS + ["all"], help="Target platform, or 'all' for every platform.")
    ap.add_argument("--out", default="./ported", help="Output root directory.")
    ap.add_argument("--dry-run", action="store_true", help="Only preview, do not write files.")
    ap.add_argument("--fix-name", action="store_true", help="Rewrite name field to match directory name.")
    ap.add_argument("--strip-output-directives", action="store_true",
                    help="Remove OpenClaw output directives (MEDIA:/[embed/[[reply_*/[[audio_as_voice]]) from text files.")
    ap.add_argument("--validate", action="store_true", help="Validate the source skill against the Agent Skills spec first.")
    ap.add_argument("--json", action="store_true", help="Output result as JSON (for automation).")
    args = ap.parse_args()

    if args.validate:
        problems = validate_skill(args.source)
        print("=== Source skill validation ===")
        if problems:
            for p in problems:
                print("  [X] " + p)
        else:
            print("  [OK] passed")
        print()

    try:
        if args.target == "all":
            results = port_skill_all(args.source, args.out, dry_run=args.dry_run,
                                     fix_name=args.fix_name,
                                     strip_output_directives=args.strip_output_directives)
        else:
            r = port_skill(args.source, args.target, args.out, dry_run=args.dry_run,
                           fix_name=args.fix_name, strip_output_directives=args.strip_output_directives)
    except ValueError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    if args.target == "all":
        if args.json:
            print(json.dumps(results, ensure_ascii=False, indent=2))
            return
        print("=== port_skill.py (all targets) ===")
        print(f"source : {Path(args.source).resolve()}")
        print()
        all_flags = []
        for t in TARGETS:
            rr = results[t]
            print(f"[{t}] files={rr['files_copied']} changed={rr['files_changed']} subs={rr['total_changes']}")
            for w in rr["warnings"]:
                print(f"  !! {w}")
            all_flags.extend(rr["flags"])
        all_flags = _dedup(all_flags)
        if all_flags:
            print()
            print(f"=== Needs manual handling (across platforms, deduplicated {len(all_flags)} item(s)) ===")
            for f in all_flags:
                print("  " + f)
        return

    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return

    print("=== port_skill.py ===")
    _print_report(r, args.dry_run)


if __name__ == "__main__":
    main()
