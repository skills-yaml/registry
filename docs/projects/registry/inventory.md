# registry Workspace Docs Inventory

Metadata:

- Adopted standard: workspace-docs@1.0.0
- Status: adoption inventory
- Owner: project
- Last reviewed: 2026-06-17

## Adopted Files

- `AGENTS.md`
- `README.md`
- `Taskfile.yml`
- `.github/workflows/ci.yml`
- `scripts/validate_registry.py`
- `scripts/test_validate_registry.py`
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

- None recorded.

## Legacy Spec Paths

- None recorded.

## Quality Gates Available

- `task check`: all repository gates.
- `task test`: deterministic validator regression tests.
- `task registry:check`: package, dependency, provenance, integrity, path, and
  released-version immutability validation, including namespace schema-2
  bundle membership when published.
- Registry CI runs `task check` for pull requests and pushes to `main`.

## Validation Run

- `git status --short` before edits: run; worktree clean.
- `task --list`: passed after the Taskfile was added.
- `task check`: passed before and after publication.
- `task test`: passed with 13 validator regression tests.
- Registry CI run `34427475083` passed on the published `main` revision.

## Notes

- Existing project-specific manual instructions remain outside generated `AGENT-CONTEXT` markers.
- Legacy specs were preserved in place.
- No secrets or environment-specific credential values were added.
