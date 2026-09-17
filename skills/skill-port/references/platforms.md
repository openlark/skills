# Target Platform Quick Reference

For each platform: skill directory location, instruction file, frontmatter differences, pitfalls.

## Contents

- [Claude Code](#claude-code)
- [Codex](#codex)
- [Cursor](#cursor)
- [Hermes Agent](#hermes-agent)
- [opencode](#opencode)
- [generic (Generic Agent Skills)](#generic)

---

## Claude Code

- **Skill directory**: project `.claude/skills/<name>/SKILL.md`; global `~/.claude/skills/<name>/SKILL.md`.
- **Instruction file**: `CLAUDE.md` (corresponds to OpenClaw's `AGENTS.md`).
- **Tools**: `Read`/`Write`/`Edit`, `Bash`, `Grep`/`Glob`, `WebFetch`/`WebSearch`, `Task` (subagent), `TaskCreate`/`TaskUpdate`.
- **frontmatter extension fields** (optional): `allowed-tools`, `disable-model-invocation`, `model`, `user-invocable`, `paths`, `disable-subagent-invocation`.
- **Pitfalls**:
  - The skill name becomes the `/name` command and can collide with built-in commands (e.g. `/review`, `/debug`).
  - `allowed-tools` uses `Bash(...)` syntax to pre-authorize commands.
  - Supports dynamic context injection `` !`command` `` (Claude Code extension, non-standard).
  - When keeping `AGENTS.md` references, they must be changed to `CLAUDE.md`.

## Codex

- **Skill directory**: `~/.codex/skills/<name>/SKILL.md`, `~/.agents/skills/<name>/SKILL.md` (project `.codex/skills/`, `.agents/skills/`).
- **Instruction file**: `AGENTS.md` (unchanged).
- **Tools**: `shell`, `apply_patch`, `spawn_agent`/`wait_agent`/`close_agent` (requires `multi_agent=true`), `update_plan`.
- **frontmatter**: standard `name` + `description` (+ optional `license`/`metadata`, etc.).
- **Pitfalls**: no `read` tool; reading files goes through `shell` (cat/grep) or the harness; see tool-mappings.md for the mapping.

## Cursor

- **Skill directory**: `.agents/skills/`, `.cursor/skills/` (project); `~/.agents/skills/`, `~/.cursor/skills/` (global). Compatible with reading `.claude/skills/`, `.codex/skills/`.
- **Instruction file**: `AGENTS.md`, `.cursor/rules/` (legacy `.cursorrules`).
- **Tools**: editor built-in `Read`/`Edit`/`Write`, `Run` (terminal), grep/glob, `Web`, `Subagent`.
- **frontmatter extension fields**: `paths` (glob scope restriction), `disable-model-invocation`, `icon`, `color`, `metadata`; legacy `globs` is deprecated.
- **Pitfalls**:
  - `paths` can restrict a skill to appear only when a matching file is present; `disable-model-invocation: true` makes the skill manual-trigger only via `/name`.
  - `Run` covers both OpenClaw's `exec` and `process` (background via `&`).
  - `Subagent` covers both `sessions_spawn` and `subagents`; reading images goes through attachments/clipboard.
  - `cron`, `sessions_*`, `memory_*`, and other OpenClaw-specific tools have no equivalents (see tool-mappings.md).

## Hermes Agent

- **Skill directory**: skill system (Skills Hub); **official migration commands exist**: `hermes claw migrate` (OpenClaw), `hermes import-agent claude-code|codex` (`~/.claude`/`~/.codex`). These migrations are the **preferred path** — this script is suited to migrating a single skill rather than an entire agent config.
- **Instruction file**: `.hermes.md`, `AGENTS.md`, `CLAUDE.md`, `SOUL.md`, `.cursorrules` (all auto-injected).
- **Tools** (official registry): `terminal`, `process`, `read_file`/`write_file`/`patch`, `web_extract`, `vision_analyze`, `memory`/`session_search`, `cronjob`, `delegate_task`, etc.
- **frontmatter**: standard `name` + `description`.
- **Closest to OpenClaw**: also has `SOUL.md`/`USER.md`/`MEMORY.md`/`AGENTS.md`, `cronjob`, heartbeat, message gateway. Porting is almost zero-change; the main difference is tool names (see the Hermes column in tool-mappings.md).
- **Pitfalls**: cross-session messages (`sessions_send`) are **handled automatically by the gateway** in Hermes — there is no agent-callable send tool — so such references can simply be deleted without rewriting them into a tool call.

## opencode

- **Skill directory**: `.opencode/skills/<name>/SKILL.md` (project); `~/.config/opencode/skills/` (global). Compatible with `.claude/skills/`, `.agents/skills/`.
- **Instruction file**: `AGENTS.md` (unchanged).
- **Tools**: `read`/`write`/`edit`, `bash`, `grep`/`glob`, `webfetch`, `skill`.
- **frontmatter extension fields**: `license`, `compatibility`, `metadata` (string→string map); unknown fields are ignored.
- **Pitfalls**: tool names are nearly identical to OpenClaw (`read`/`write`/`edit` unchanged); differences are in tool-mappings.md.

## generic (Generic Agent Skills)

- **Goal**: keep only the common subset of the Agent Skills standard (agentskills.io), usable on any platform.
- **frontmatter**: only `name` + `description` (optional `license`/`compatibility`/`metadata`).
- **Content**: remove all tool-name references, platform-specific directives, `MEDIA:`/`[embed`/`[[reply_*`; rewrite `exec` etc. into neutral "run command" descriptions.
- **Use case**: as a "lowest common denominator" artifact, or for publishing to multi-platform skill marketplaces (ClawHub / agentskills.io ecosystem).

## Place + Validate

- Place: copy the `<name>/` directory from the output to the target platform's skill directory (see table above).
- Validate: use the Agent Skills standard validator `skills-ref validate <skill-dir>` (see agentskills.io/specification); or skill-creator's `quick_validate.py`.
