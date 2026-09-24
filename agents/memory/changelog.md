# Memory Changelog

## 2026-06-17 - Initialize Agent Memory

- Type: fact
- Source: user
- Confidence: high
- Review: none
- Supersedes: none

Content:

Initialized `agents/memory/` for registry during additive adoption of `workspace-docs@1.0.0`.

## 2026-09-10 - Record Workspace registry publication contract

- Type: decision
- Source: user
- Confidence: high
- Review: none
- Supersedes: none

Content:

Recorded the independently versioned `workspace/<skill-id>` namespace,
immutable exact versions, contained aliases, exact dependency metadata,
release-set manifest, and CI-enforced validation contract in
`agents/memory/decisions.md`.

## 2026-09-10 - Record Workspace lifecycle package publication

- Type: fact
- Source: command
- Confidence: high
- Review: none
- Supersedes: none

Content:

Recorded the 19-package Workspace toolkit 0.3.0 publication, canonical source
and registry commits, passing main CI, and successful SKM 0.4.0 dependency
install, check, and convergent reapply in `agents/memory/facts.md`.

## 2026-09-19 - Redact Host Service Inventory

- Type: decision
- Source: user
- Confidence: high
- Review: none
- Supersedes: none

Content:

`system/devops-manager@1.0.0` published a private host's service inventory to a
public repository. It was withdrawn and replaced by 1.1.0, and the registry
gained the withdrawal mechanism recorded in decisions.

## 2026-09-24 - Select Registry Bundle Metadata For Workspace Install-All

- Type: decision
- Source: user
- Confidence: high
- Review: after schema-2 publication
- Supersedes: instructionless metapackage design

Content:

Recorded the Registry namespace-bundle decision and schema-2 validation
contract in `agents/memory/decisions.md`. Workspace publication has not been
claimed.

## 2026-09-24 - Generate Namespace Manifests

- Type: decision
- Source: user
- Confidence: high
- Review: none
- Supersedes: none

Content:

Added `scripts/generate_manifests.py` and `task manifest`, and published the
`skills-yaml/authoring-toolkit` bundle through a generated manifest.
