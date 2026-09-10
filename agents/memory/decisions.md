# Decisions

## 2026-06-17 - Adopt workspace-docs@1.0.0

- Type: decision
- Source: user
- Confidence: high
- Review: none
- Supersedes: none

Content:

registry adopts the workspace documentation standard at `workspace-docs@1.0.0`. Adoption is additive: preserve project-specific guidance and legacy specs, and keep generated agent context inside `AGENT-CONTEXT` markers.

## 2026-09-10 - Publish Workspace skills as independent immutable packages

- Type: decision
- Source: user
- Confidence: high
- Review: none
- Supersedes: none

Content:

Workspace lifecycle skills use the `workspace/<skill-id>` registry namespace
and independent semantic versions. Exact version directories are immutable;
root/current content follows `latest`; `latest` and `default` are contained
aliases; and exact same-registry dependencies live in the Agent Skills string
metadata map. A namespace manifest records the tested release set, canonical
source revision, and Workspace, SKM, and adapter compatibility. Registry CI
enforces structure, provenance, source integrity, dependency, path, alias, and
released-version immutability checks.
