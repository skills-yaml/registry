# Spec: Agent Portability Baseline For Registry Skills

Status: Backlog

Purpose: Guarantee that a skill published here installs and loads correctly in
every agent SKM links into, and record the compatibility rules that guarantee
holds.

## 1. Problem Statement

This registry publishes skills that SKM links into agent skill directories. As
of 2026-09-21 that means sixteen agents across seven vendors and nine
open-source projects, each with its own `SKILL.md` expectations.

Those expectations conflict:

- **`name` required**: Codex, Cursor, Copilot, OpenCode, Roo Code and Kilo Code
  require it. Claude Code, Antigravity and Grok treat it as optional and default
  to the directory name.
- **`name` must match its directory**: OpenCode requires it. Pi deliberately
  allows them to differ, calling the rule "suboptimal for shared skill
  directories used across multiple agent harnesses".
- **`name` character set**: Copilot requires lowercase with hyphens. OpenCode
  requires 1–64 characters, lowercase alphanumeric, single hyphen separators, no
  leading, trailing or consecutive hyphens.
- **`description` required**: Codex, Cursor, Copilot, OpenCode, Roo Code and
  Antigravity require it. Claude Code calls it recommended. Grok makes it
  optional.
- **`description` length**: Claude Code allows 1,536 characters including
  `when_to_use`. Roo Code documents 1–1024.
- **Unknown keys**: Grok and OpenCode ignore them explicitly. Others do not say.

Nothing in the repository records which of these the registry targets, so a
future change to `scripts/validate_registry.py` could relax a rule that some
agent depends on, and no reviewer would notice.

## 2. Goals and Non-Goals

### Goals

- State the portability baseline as the strict intersection of what the
  supported agents accept.
- Confirm the current validator already enforces it, or add what is missing.
- Record the conflicts above so the baseline can be re-derived when an agent
  changes its rules.
- Document how registry metadata survives agents that do not know about it.

### Non-Goals

- Changing where SKM links skills. That is
  `workspace/specs/backlog/agents/agent-skill-directory-integration.md` in the
  SKM repository.
- Publishing per-agent skill variants. One `SKILL.md` must satisfy every agent.
- Adopting any agent-specific frontmatter field, such as Claude Code's
  `allowed-tools` or Cursor's `icon`. A skill needing those is not portable and
  does not belong in this registry.

## 3. Proposed Design

### The baseline

A published `SKILL.md` must satisfy all of:

| Rule | Set by the strictest agent |
| --- | --- |
| `name` present | Codex, Cursor, Copilot, OpenCode, Roo, Kilo |
| `name` matches the containing directory | OpenCode |
| `name` is 1–64 chars, lowercase alphanumeric, single hyphens, no leading, trailing or consecutive hyphen | OpenCode, Copilot |
| `description` present and non-empty | Codex, Cursor, Copilot, OpenCode, Roo, Antigravity |
| `description` at most 1024 characters | Roo Code |
| Registry-specific values live under `metadata` as strings | Cursor, Grok, OpenCode |

The validator enforces five of these six today. Presence of `name`, the
directory match, the character set, `description` presence, the 1024-character
description cap, and the string-typed `metadata` map are all checked.

**The 64-character name cap is not enforced.** `NAME_PATTERN` at
`scripts/validate_registry.py:24` is `[a-z0-9]+(?:-[a-z0-9]+)*`, which constrains
the character set and hyphen placement but not length: a 70-character name passes
today and would be rejected by OpenCode at install time. Closing that gap is the
one code change this specification requires.

Beyond it, the product is the written justification rather than new code: today
the rules look arbitrary, and the first person to find one inconvenient has no
way to know what it protects.

Pi's relaxation of the directory-match rule does not weaken the baseline. A
skill whose name matches its directory is valid in Pi too; the intersection
still holds.

### Metadata portability

Registry values are carried as strings under `metadata` (`skm-version`,
`skm-dependencies`, and Workspace provenance keys). Grok and OpenCode document
that unknown frontmatter is ignored, and `metadata` is an accepted field in
Cursor and Grok. No supported agent is documented to reject it. Agents that do
not understand the keys simply do not act on them, which is the intent.

### Recording the baseline

1. Enforce the 64-character cap on skill and namespace names, with a test that a
   65-character name is rejected.
2. Add a `## Agent Portability` section to `SKILL_STRUCTURE.md` holding the table
   above, each rule attributed to the agent that requires it, with links.
3. Add a comment block at the head of the frontmatter checks in
   `scripts/validate_registry.py` pointing at that section, so the next person to
   change a limit reads the reason first.
4. Record the supported-agent list and the date it was verified, because these
   rules move: this baseline is a snapshot of 2026-09-21 documentation.

### Review trigger

The baseline is re-derived when SKM adds an agent, or when a supported agent
changes its `SKILL.md` rules. Adding an agent that is stricter than the current
intersection is a breaking change for already-published skills and requires its
own spec; adding a more permissive one requires no change.

## 4. Verification and Acceptance Criteria

- [ ] A name longer than 64 characters is rejected, with a regression test.
- [ ] `SKILL_STRUCTURE.md` states the baseline, attributes each rule, and links
      to the documentation it came from.
- [ ] The validator's frontmatter checks reference that section.
- [ ] Every currently published skill satisfies the baseline once the length cap
      is enforced. The longest published name is well under the limit, so no
      existing package should need renaming; confirm before merging, because a
      rename would be a breaking change requiring a withdrawal under
      `WITHDRAWN.yaml`.
- [ ] The supported-agent list and verification date are recorded.
- [ ] `task check` and `task test` pass.

## 5. Risks and Mitigations

- *Risk*: The baseline is recorded once and rots as agents change their rules.
  *Mitigation*: The review trigger names the two events that invalidate it, and
  the recorded date makes staleness visible rather than silent.
- *Risk*: A contributor reads the baseline as the registry endorsing the
  strictest agent's preferences.
  *Mitigation*: Each rule is attributed, so the cost of relaxing it is legible:
  the agents that would break are named.
