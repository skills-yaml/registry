# Project Structure

Metadata:

- Standard: workspace-docs@1.0.0
- Status: static
- Owner: project
- Last reviewed: 2026-06-17

## Scope

This document records the repository layout and ownership boundaries for `registry`.

## Source Of Truth

- `README.md`
- Root source directories and configuration files
- `docs/projects/registry/inventory.md`

## Required Rules

- Follow the existing directory layout and nearest local pattern.
- Keep generated workspace-docs context inside generated markers.
- Keep legacy specs in place unless a separate migration is explicitly requested.

## Workflow

1. Read `README.md` and `AGENTS.md` before changing structure.
2. Identify the smallest project area affected by a change.
3. Update this document when durable ownership or layout boundaries change.

## Validation

- New files are placed under the documented project area.
- Required docs and state folders listed in the project inventory exist.

## References

- `AGENTS.md`
- `README.md`
- `docs/projects/registry/inventory.md`
