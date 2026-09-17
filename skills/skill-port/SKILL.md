---
name: skill-port
description: Ports/adapts OpenClaw skills to other agent platforms (Claude Code, Codex, Cursor, Hermes, opencode, generic Agent Skills). 
---

# Porting OpenClaw Skills Across Platforms

Convert an OpenClaw skill into one that works correctly on other agent platforms.
Rewrites platform coupling points: tool-name references, system files (AGENTS.md→CLAUDE.md), output directives (MEDIA:, [embed], etc.), platform-specific tools (cron, sessions_*, memory_*), and paths, and normalizes frontmatter. Use when the user wants to port/adapt/convert an OpenClaw skill. Trigger words: port skill, adapt skill, convert skill.

## Core Insight

An OpenClaw skill's **structure is already compatible with the Agent Skills standard** (`SKILL.md` + frontmatter + `references/`/`scripts/`/`assets/`), and every platform reads `<dir>/skills/<name>/SKILL.md` directly. **The real adaptation work lies in the platform coupling inside the content, not the structure.** Pure knowledge/content skills need almost zero changes; only skills that reference platform tools or OpenClaw-specific features require substantive rewriting.

## Quick Decisions

- **Pure knowledge/content** (no tool references, no `MEDIA:`/`cron`/`sessions_*`) → copy directly + normalize frontmatter.
- **References tools/platform-specific features** → run `port_skill.py` for mechanical replacement, then handle remaining items manually per the report.
- Run `--dry-run` first to preview, confirm, then actually write files.

## Workflow

1. **Confirm the target platform** — `claude-code` / `codex` / `cursor` / `hermes` / `opencode` / `generic`. See [platforms.md](references/platforms.md) for directory locations, instruction files, and frontmatter pitfalls.
2. **Inventory coupling points** — tool-name references, system files (`AGENTS.md`→`CLAUDE.md`), `MEDIA:`/`[embed`/`[[reply_*`, `cron`/`sessions_*`/`memory_*`, and `~/.openclaw/workspace` paths. See [openclaw-specifics.md](references/openclaw-specifics.md).
3. **Run the conversion**:
   ```bash
   python3 scripts/port_skill.py --source ~/.openclaw/workspace/skills/<name> --target <platform> --out ./ported --dry-run
   ```
   After confirming the diff, drop `--dry-run`; use `--target all` to do all platforms at once. See [example.md](references/example.md) for a complete example.
4. **Manual review** — handle the "needs manual handling" items in the report (`cron`, cross-session messages, attachment directives).
5. **Place + validate** — put it in the target platform's skill directory and use a validator to confirm `SKILL.md` is valid.

## Script Usage

`scripts/port_skill.py` performs deterministic conversion: tool names → system files/paths → frontmatter normalization → outputs a "needs manual handling" report.

Arguments: `--target claude-code|codex|cursor|hermes|opencode|generic|all`, `--dry-run` (preview), `--strip-output-directives` (automatically remove `MEDIA:`/`[embed`/`[[reply_*]]`/`[[audio_as_voice]]`), `--fix-name` (fix a name that doesn't match the directory name), `--validate`, `--json`.

Replacement precision: short English words (`read`/`write`/`exec`/`image`…) are replaced only inside backticks; non-English words (`sessions_*`/`memory_*`/`web_fetch`…) are replaced as bare words; `AGENTS.md` is rewritten to `CLAUDE.md` only for Claude Code. See [tool-mappings.md](references/tool-mappings.md) for the full mapping.

## Reference Files

| File | Content | When to read |
|---|---|---|
| [tool-mappings.md](references/tool-mappings.md) | Full tool/file/path mapping | When performing replacements, writing scripts |
| [openclaw-specifics.md](references/openclaw-specifics.md) | Classification and handling of platform-specific features | When inventorying coupling points |
| [platforms.md](references/platforms.md) | Per-platform directory/instructions/frontmatter/pitfalls | When confirming the target platform |
| [example.md](references/example.md) | Complete before/after comparison example | First time getting started |
