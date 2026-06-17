# SDLC

Metadata:

- Standard: workspace-docs@1.0.0
- Status: static
- Owner: project
- Last reviewed: 2026-06-17

## Scope

This document records the development lifecycle expected for the `registry` project.

## Source Of Truth

- `AGENTS.md`
- `README.md`
- `docs/specs/`
- Existing project process docs when present.

## Required Rules

- Tie non-trivial work to a spec.
- Use `docs/specs/backlog/`, `docs/specs/development/`, and `docs/specs/done/` for new workspace-aligned specs.
- Preserve existing legacy specs until a separate migration explicitly moves them.
- Run available quality gates before marking work complete.

## Workflow

1. Clarify scope, acceptance criteria, and validation gates.
2. Put active non-trivial work in `docs/specs/development/`.
3. Implement narrowly against the accepted scope.
4. Run available checks and tests.
5. Move completed specs to `docs/specs/done/` only after implementation, docs, and validation are reconciled.

## Validation

- Relevant spec exists in the correct state.
- Project gates pass or skipped gates are documented.
- Durable facts or decisions are recorded in `agents/memory/` when needed.

## References

- `AGENTS.md`
- `README.md`
- `docs/projects/registry/inventory.md`
