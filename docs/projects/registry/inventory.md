# registry Workspace Docs Inventory

Metadata:

- Adopted standard: workspace-docs@1.0.0
- Status: adoption inventory
- Owner: project
- Last reviewed: 2026-06-17

## Adopted Files

- `AGENTS.md`
- `README.md`
- `docs/tech/task.md`
- `docs/tech/sdlc.md`
- `docs/tech/project_structure.md`
- `docs/specs/README.md`
- `docs/specs/backlog/`
- `docs/specs/development/`
- `docs/specs/done/`
- `docs/standards/workspace-docs/README.md`
- `agents/memory/README.md`
- `agents/memory/decisions.md`
- `agents/memory/facts.md`
- `agents/memory/preferences.md`
- `agents/memory/open-questions.md`
- `agents/memory/changelog.md`

## Missing / Known Gaps

- No Taskfile exists; task/check/test gates are not currently defined.

## Legacy Spec Paths

- None recorded.

## Quality Gates Available

- No Taskfile detected.

## Validation Run

- `git status --short` before edits: run; worktree clean.
- `task --list`: skipped; no Taskfile detected.
- `task check`: skipped; no Taskfile detected.
- `task test`: skipped; no Taskfile detected.

## Notes

- Existing project-specific manual instructions remain outside generated `AGENT-CONTEXT` markers.
- Legacy specs were preserved in place.
- No secrets or environment-specific credential values were added.
