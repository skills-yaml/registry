# Project Guidelines (registry)

<!-- AGENT-CONTEXT:START workspace-docs@1.0.0 -->
## Workspace Documentation Standard

This project follows `workspace-docs@1.0.0`.

### Required Reading

- `AGENTS.md`
- `README.md`
- `docs/tech/task.md`
- `docs/tech/sdlc.md`
- `docs/tech/project_structure.md`
- Relevant conditional docs under `docs/tech/`
- Relevant specs under `docs/specs/`
- Project memory under `agents/memory/` when present

### Spec-Driven Development

Every non-trivial change must be tied to a spec.

Specs live in one state:

- `docs/specs/backlog/`
- `docs/specs/development/`
- `docs/specs/done/`

Allowed transitions:

- `backlog -> development`
- `development -> done`

Do not start implementation until the development spec has scope, acceptance criteria, affected areas, and validation gates.

### Documentation Boundaries

Static docs are project-owned and must not be rewritten by automation.

Generated agent context must stay between `AGENT-CONTEXT` markers. Manual project rules must stay outside generated blocks.

### Agent Memory

Durable project memory belongs in `agents/memory/`.

Record only stable facts, decisions, preferences, and open questions. Do not store secrets, tokens, credentials, or transient scratch notes.
<!-- AGENT-CONTEXT:END -->

## Project Scope

Registry of reusable skills and agents for the skm ecosystem.

## Required Reading

- `README.md`
- `docs/tech/task.md`
- `docs/tech/sdlc.md`
- `docs/tech/project_structure.md`
- `docs/specs/README.md`
- `agents/memory/README.md`

## Local Rules

- Preserve project-specific documentation and legacy specs unless a separate migration explicitly changes them.
- Use available task gates for validation and document any skipped gate with the reason.

### Branch Model

- `develop` is the integration branch. Changes land here first.
- `main` is the production branch and the published state of the registry. A
  consumer pinning a skill resolves against `main`.
- Release by merging `develop` into `main`. Do not commit to `main` directly.

A spec moves to `done` only after the change is released through `main`.
Integration into `develop` is not release: a skill merged to `develop` is not yet
installable by consumers. Record both events in the spec.

Released-version immutability is enforced against `origin/main`, so a published
exact version stays immutable from the moment it reaches production, not from
the moment it reaches `develop`.
