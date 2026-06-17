# Task

Metadata:

- Standard: workspace-docs@1.0.0
- Status: static
- Owner: project
- Last reviewed: 2026-06-17

## Scope

This document records the task-runner contract for the `registry` project.

## Source Of Truth

- `Taskfile.yml`, `Taskfile.yaml`, or equivalent files when present.
- `README.md` for documented setup and local commands.

## Required Rules

- Prefer project task entrypoints over ad hoc commands when a Taskfile exists.
- If no Taskfile exists, document that gap in `docs/projects/registry/inventory.md` before relying on direct tool commands.
- Do not add environment-specific secrets or credentials to task definitions.

## Workflow

1. Run `task --list` or `task --list-all` when a Taskfile exists.
2. Use the narrowest task that validates the affected area.
3. Record skipped gates and reasons in the project inventory or completing spec.

## Validation

- `task --list` when a Taskfile exists.
- `task check` when defined and dependencies are available.
- `task test` when defined and dependencies are available.

## References

- `AGENTS.md`
- `README.md`
- `docs/projects/registry/inventory.md`
