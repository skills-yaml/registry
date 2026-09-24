# Frontmatter That Works In Every Agent

A published skill is installed into many agents, and their `SKILL.md` rules
conflict. Staying inside the intersection means one file works everywhere.

## The portable subset

| Rule | Required by |
| --- | --- |
| `name` present | Codex, Cursor, Copilot, OpenCode, Kilo Code |
| `name` equals the containing directory | OpenCode |
| `name` 1–64 chars, lowercase alphanumeric, single hyphens | OpenCode, Copilot |
| `description` present and non-empty | Codex, Cursor, Copilot, OpenCode, Antigravity |
| `description` at most 1024 characters | Roo Code, Kilo Code |
| Registry values as strings under `metadata` | Cursor, Grok, OpenCode |

Claude Code and Antigravity treat `name` as optional, defaulting to the directory
name, and Grok makes both optional. Following the stricter rule satisfies all of
them. Pi deliberately allows `name` to differ from its directory; matching it
anyway is valid there too.

Claude Code allows a longer description than 1024 characters, but Roo Code and
Kilo Code do not, so 1024 is the limit that binds first.

## Fields to avoid in a published skill

These are real fields in specific agents, and each one costs portability:

- `allowed-tools` — Claude Code, Copilot, Grok
- `icon`, `color` — Cursor
- `paths` / `globs` — Claude Code, Cursor, Grok, OpenHands
- `disable-model-invocation`, `user-invocable` — Claude Code, Cursor, Grok
- `context`, `agent`, `model`, `effort`, `arguments` — Claude Code

Agents that do not know a field generally ignore it, but nothing guarantees that,
and a skill that depends on one only behaves correctly in the agent that defines
it. A skill needing agent-specific behavior is not portable; keep it local rather
than publishing it.

## Unknown keys

Grok and OpenCode document that unknown frontmatter is ignored. Others do not say
either way. The `metadata` map is the sanctioned place for registry values, so
put them there rather than at the top level.

## Writing the description

The description is the only thing most agents read before deciding whether to
load the skill. Write it for that decision:

- Say what the skill does, then the situations that should trigger it.
- Name the concrete artifacts and verbs a user would say.
- Do not describe the implementation, and do not sell it.

A description that says only what a thing is, with no trigger conditions, loads
rarely and looks broken to the user who installed it.
