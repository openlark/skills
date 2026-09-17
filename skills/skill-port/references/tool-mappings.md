# Tool Name & File & Path Mappings (Full)

> OpenClaw tool names → equivalent tool names for each target platform. `—` means the platform has no direct equivalent and the reference must be rewritten manually or deleted.

## 1. File/Command Tools

| OpenClaw | Claude Code | Codex | Cursor | Hermes | opencode | generic |
|---|---|---|---|---|---|---|
| `read` | `Read` | `shell` (`cat`) | Read | `read_file` | `read` | read file |
| `write` | `Write` | `apply_patch` / `shell` | Write | `write_file` | `write` | write file |
| `edit` | `Edit` | `apply_patch` | Edit | `patch` | `edit` | edit file |
| `exec` | `Bash` | `shell` | Run / Terminal | `terminal` | `bash` | run command |
| `process` | `Bash` (background `&`) | `shell` (background) | Run (background) | `process` | `bash` (background) | background command |
| `web_fetch` | `WebFetch` | `shell` (`curl`) | Web / WebFetch | `web_extract` | `webfetch` | fetch URL |
| `image` | `Read` (with attachment) | `Read` (with attachment) | read image / attachment | `vision_analyze` | read image / attachment | read image |

## 2. Subagent / Session Tools

| OpenClaw | Claude Code | Codex | Cursor | Hermes | opencode | generic |
|---|---|---|---|---|---|---|
| `sessions_spawn` | `Task` / `Agent` | `spawn_agent` | Subagent | `delegate_task` | task / agent | spawn subagent |
| `subagents` | `Task` / `Agent` | `spawn_agent` | Subagent | `delegate_task` | task / agent | manage subagents |
| `sessions_list` | `Task` (list) | — | — | — | — | list sessions |
| `sessions_history` | — | — | — | `session_search` | — | session history |
| `sessions_send` | — | — | — | message gateway | — | cross-session message |
| `sessions_yield` | — | — | — | — | — | yield turn |

> Cross-session messages (`sessions_send`) are a gateway feature of OpenClaw/Hermes; Claude Code/Codex/Cursor/opencode have no direct equivalent. Such references must be **rewritten manually** into an intra-platform mechanism (e.g. a Task return value, file exchange), or deleted outright.

## 3. OpenClaw-Specific Tools

| OpenClaw tool | Handling strategy |
|---|---|
| `cron` | Only Hermes has `cronjob`. Other platforms `—`: rewrite manually to an external scheduler or platform equivalent (Claude Code has no built-in cron). |
| `memory_get` / `memory_search` | Hermes uses the `memory` tool. Other platforms use "read file" as a substitute; rewrite references to Read/read_file reading the corresponding md. |
| `session_status` | OpenClaw-specific. Claude Code uses `/status`, `/context`; other platforms rewrite manually or delete. |
| `channel-push` / `feishu-*` / `tbox*` / `redbook` | OpenClaw platform-extension skills, **not portable** — depend on the OpenClaw gateway/extension. Mark as not applicable and skip the whole skill. |

## 4. System File References

| OpenClaw file | Handling |
|---|---|
| `AGENTS.md` | Only Claude Code changes it to `CLAUDE.md`; other platforms keep it (Hermes may use `.hermes.md`, Cursor may use `.cursor/rules`). |
| `SOUL.md`/`USER.md`/`MEMORY.md`/`HEARTBEAT.md` | OpenClaw/Hermes-specific persona/memory files, absent on other platforms — rewrite references to "project rules file" or delete. |
| `TOOLS.md`/`IDENTITY.md`/`BOOTSTRAP.md` | No equivalent on any platform; delete the references. |

## 5. Path References

| OpenClaw path | Handling |
|---|---|
| `~/.openclaw/workspace` | No cross-platform equivalent. Rewrite to a relative path or the target platform's project root; the script only flags it, never blind-rewrites. |
| `~/.openclaw/workspace/skills/` | Maps to the target skill directory (see platforms.md). |
| `~/openclaw/skills/` | Same as above. |

## 6. Frontmatter Normalization

| Field | Handling |
|---|---|
| `name` | Keep (must match the directory name, 1–64 characters, lowercase + hyphens). |
| `description` | Keep (1–1024 characters). |
| `allowed-tools` | Agent Skills standard (experimental). Claude Code syntax `Bash(x)`/`Read`, etc.: **kept as-is only for the claude-code target**, removed for other targets. |
| Other fields | **Keep** (e.g. `license`/`metadata`/`compatibility`, explicitly supported by opencode/Cursor; unknown fields are ignored by the target platform). The script only removes `allowed-tools`. |

Generic frontmatter keeps only `name` + `description` (may add `license`/`metadata`/`compatibility`; see platforms.md).
