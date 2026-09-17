# Example: Porting a Skill (Before / After)

Using a hypothetical skill `img-caption` as an example, demonstrating a complete conversion to Claude Code.

## Source Skill (OpenClaw)

```
img-caption/
├── SKILL.md
└── references/usage.md
```

**SKILL.md**
```markdown
---
name: img-caption
description: Batch-generates captions for images. Uses the `image` tool for recognition and `write` to output JSON.
allowed-tools: Bash(python:*)
---

# Image Caption Generation

1. Use the `image` tool to analyze the image
2. Use `write` to save the result to caption.json
3. Use `exec` to run the post-processing script
```

**references/usage.md**
```markdown
## Batch Processing
Loop over `sessions_spawn` to process subtasks in parallel.
The script lives under `~/.openclaw/workspace/scripts/`.
```

## Run

```bash
python3 scripts/port_skill.py --source img-caption --target claude-code --out ./ported
```

## Output Skill (Claude Code)

```
ported/claude-code/img-caption/
├── SKILL.md
└── references/usage.md
```

**SKILL.md** (`allowed-tools` kept, tool names rewritten)
```markdown
---
name: img-caption
description: Batch-generates captions for images. Uses the `Read` tool for recognition and `Write` to output JSON.
allowed-tools: Bash(python:*)
---

# Image Caption Generation

1. Use the `Read` tool to analyze the image
2. Use `Write` to save the result to caption.json
3. Use `Bash` to run the post-processing script
```

**references/usage.md** (`sessions_spawn`→`Task`, path flagged for manual handling)
```markdown
## Batch Processing
Loop over `Task` to process subtasks in parallel.
The script lives under `~/.openclaw/workspace/scripts/`.
```

## Report Excerpt

```
files  : 2 copied, 2 changed (5 substitutions)

=== Needs manual handling (1 item) ===
  references/usage.md:3: [~/.openclaw] The script lives under `~/.openclaw/workspace/scripts/`.
```

## Notes

- The `` `image` `` in `description` was also rewritten to `Read` — if you want to preserve the original meaning (e.g. the sentence is explaining a concept), change it back. The script is "mechanical replacement + report", with a human making the final call.
- The absolute path `` `~/.openclaw/workspace/scripts/` `` has no cross-platform meaning; the report flags it, and it must be manually changed to a relative path or the target platform's equivalent location.
- In this example `sessions_spawn` → `Task` is an approximate mapping: Claude Code's `Task` is used for subagents, semantically close, but the parameters differ, so complex usages still need manual adjustment.

---

## Multi-Platform Quick Differences

Porting the same skill to different platforms differs only in tool names; the flow is identical. Key differences:

- **Cursor**: `exec`→`Run`, `web_fetch`→`Web`, `sessions_spawn`→`Subagent`; no equivalents for `cron`/`sessions_send`/`memory_*`.
- **Codex**: `read`/`exec`→`shell`, `write`→`apply_patch`, `sessions_spawn`→`spawn_agent`.
- **Generic**: all tool names are replaced with neutral descriptions (`exec`→`run command`, `image`→`read image`).
- **opencode**: tool names are almost identical to OpenClaw, only `exec`→`bash`, `web_fetch`→`webfetch`.

See [tool-mappings.md](tool-mappings.md) for the full mapping.

For skills containing `MEDIA:` and other output directives, add `--strip-output-directives` to remove them automatically:

```bash
python3 scripts/port_skill.py --source <name> --target codex --out ./ported --strip-output-directives
```
