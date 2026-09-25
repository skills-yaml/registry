# Specs

registry follows `workspace-docs@1.0.0` for new spec state management.

Canonical state directories:

- `backlog/`: accepted ideas that are not actively being implemented.
- `development/`: active work with scope, acceptance criteria, affected areas, implementation plan, validation gates, and risks.
- `done/`: completed work with final behavior and validation recorded.

Allowed transitions:

- `backlog -> development`
- `development -> done`

This repository's configured branch targets are:

- integration: `develop`
- production: `main`

A branch name alone is not lifecycle evidence. `done` requires a confirmed
release through `main`; record the integration and release events in the spec.

## Backlog

- [Agent Portability Baseline For Registry Skills](backlog/agent-portability-baseline.md)

## Active Specs

None.

## Completed Specs

- [Publish Workspace Skill Bundles](done/publish-workspace-skill-bundles.md)
- [Generate Namespace Manifests](done/generate-namespace-manifests.md)
- [Adopt `develop` As The Integration Branch](done/adopt-develop-integration-branch.md)
- [Publish The `skills-yaml` Authoring Namespace](done/publish-skill-authoring-namespace.md)
- [Publish Workspace Lifecycle Skills](done/publish-workspace-lifecycle-skills.md)
- [Remove Host Service Inventory From The Public Registry](done/redact-host-service-inventory.md)
- [Add gcp-debug Skill To Registry](done/gcp-debug-spec.md)

Legacy or reference spec paths preserved during adoption:

- None recorded.

Do not move or rewrite legacy specs unless a separate migration explicitly requests it.
