# OpenClaw-Specific Features and Handling Strategy

Inventory the platform coupling points that may appear in OpenClaw skill content, organized into three categories: auto-replaceable / needs manual rewrite / not portable.

## A. Output Directives (delete or rewrite)

OpenClaw's assistant output directives are not recognized by other platforms and should be **deleted** (or rewritten to the target platform's equivalent mechanism):

| Directive | Meaning | Handling |
|---|---|---|
| `MEDIA:<path>` | Attachment delivery marker | Delete the line; or rewrite as "attachment: read file `<path>` and hand it to the user" |
| `[embed ...]` | Inline rendering in webchat | Delete (only effective in Control UI/webchat) |
| `[[reply_to_current]]` | Reply-reference marker | Delete (each platform has a different reply mechanism) |
| `[[reply_to:<id>]]` | Directed reply reference | Delete |
| `[[audio_as_voice]]` | Voice-note hint marker | Delete |

## B. Platform-Specific Tools (needs manual rewrite)

| Feature | Portable to | Handling |
|---|---|---|
| `cron` (scheduled tasks) | Hermes (has `cron`) | Other platforms: rewrite to an external cron/systemd/platform scheduler; or delete the capability description. |
| `sessions_send` (cross-session messages) | Hermes (message gateway) | Other platforms: rewrite to a Task return value / file exchange / delete outright. |
| `memory_get` / `memory_search` (persistent memory) | Hermes (MEMORY.md) | Other platforms: rewrite to "read file". |
| `session_status` (session status card) | none | Delete; Claude Code uses `/status`. |
| `sessions_history` (cross-session history) | Hermes | Other platforms: delete. |

## C. Non-Portable Skills (skip the whole skill)

Skills that depend on OpenClaw gateway/extension/platform capabilities are pointless to port:

- `channel-push` — depends on OpenClaw message-channel push
- `feishu-*` (feishu-doc/drive/perm/wiki) — depends on the Feishu extension
- `tbox*` (tbox-ppt-skill / tbox-share-remix / tbox-skill-import / tboxhub / TboxBook) — depends on the Tbox platform
- `redbook` — depends on the Xiaohongshu platform extension
- Any skill that references a `~/.openclaw/...` runtime feature that does not exist on the target platform

> Decision criterion: read the skill's `SKILL.md`. If its core capability is bound to the OpenClaw gateway/extension, mark it as "not applicable" and do not force a port.

## D. Model Aliases (delete or rewrite)

Model aliases injected by the OpenClaw environment (such as `tbox-ai/deepseek-v4-pro-0813`, `glm-5.3`, etc.) are OpenClaw-specific configuration. If such aliases appear in a skill, rewrite them to the target platform's model identifier or delete them outright.

## E. Cases Requiring No Changes

- Pure knowledge/content skills (tutorials, templates, specs, API references): usable after frontmatter normalization, content almost untouched.
- `references/`, `scripts/`, `assets/` directory structure: fully compatible with the Agent Skills standard, copy directly.
- Generic programming/writing instructions (not referencing any platform tools): keep as-is.

## Handling Priority Cheat Sheet

1. Run `port_skill.py` first (auto-handles: backticked tool names, bare non-English tool names, `AGENTS.md→CLAUDE.md`, frontmatter).
2. Then read the script report and handle `MEDIA:`/`[embed`/`[[reply_*`/`cron`/`sessions_send`/`memory_*`/paths item by item.
3. Finally determine whether it belongs to category C "not portable"; if so, skip the whole skill.
