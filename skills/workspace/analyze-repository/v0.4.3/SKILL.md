---
name: analyze-repository
description: Analyze a repository without modifying it, producing an evidence-backed account of its purpose, structure, technology stack, development lifecycle, policies, documentation state, active work, risks, and evidence gaps. Use when a repository needs assessment, onboarding context, or current-state discovery before planning work.
metadata:
  skm-version: "0.4.3"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "ea074843f54a3197ae9adf8ada2e770c0caa862c"
  skm-source-path: "workspace/instructions/skills/analyze-repository"
  skm-source-integrity: "sha256:06cbde68d0eb723b1c20fe42107c6ee5dffc22b797db637f9cae8ff439d51728"
  workspace-toolkit-version: "0.12.0"
  workspace-docs-compatibility: "8.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/design-domain-model@0.1.3"
---

# Analyze Repository

Build a current-state report from repository evidence. Remain read-only.

## Establish Scope

1. Read the repository's agent policy and its required documentation before
   inspecting implementation details.
2. Confirm the repository root and requested analysis scope. Inspect only the
   current project; do not inventory sibling projects or machine-local state.
3. Preserve the distinction between observed facts, documented intent,
   reasonable inferences, and unresolved evidence gaps.

## Analyze

Inspect the smallest sufficient set of sources to establish:

- repository purpose, major components, and ownership boundaries;
- languages, frameworks, package managers, runtime requirements, and generated
  artifacts;
- canonical build, test, lint, validation, and task-runner entrypoints;
- Workspace standard version, applicable instructions, active specifications,
  documentation state, and durable memory state when present;
- source-control, CI/CD, release, migration, and rollback conventions;
- security-sensitive boundaries, untrusted inputs, secrets handling, and
  dependency or supply-chain exposure; and
- inconsistencies, stale documentation, missing evidence, and material risks.

Use repository-native, read-only commands. Do not install dependencies, execute
untrusted project resources, mutate infrastructure, or infer delivery status
from a branch name alone.

## Report

Lead with the repository's current status and the most consequential findings.
Include concise evidence using repository-relative paths, identify commands
that were actually run, and state limitations. Recommend next actions only
when they follow directly from the evidence. Do not edit files, create specs,
or persist memory while operating in this skill.

## Assess Existing Modeling Evidence

When domain/data/schema architecture is relevant, identify existing glossaries,
context/ownership decisions, logical models, contracts, migrations and their
consumers. Distinguish observed structure from intended business behavior; names
and absent diagrams are not evidence of correctness or nonconformance. For a
focused modeling assessment use $design-domain-model in read-only assess mode.
Do not create design artifacts or infer unapproved domain rules during analysis.

## Pinned Lifecycle Assessment

Assess the actual pinned contract. For v7, distinguish local implementation,
confirmed shared-test integration, verified main completion with reconciled
acceptance/records, and separate deployment/publication. Inspect blocked reason,
kind, prior stage, and resume condition without changing lifecycle states.
Check whether modular gate inputs, dependencies, consumers, resource constraints,
and freshness justify affected iteration and full final coverage after review.
Assess staged development evidence: changed-component checks must pass before
checks of affected direct/transitive consumers in dependency order. Inspect
contract and side-effect impact, missing coverage/tools, fallback reasons,
old/new dependencies for renames/deletions, overlapping changes, cycles, and
freshness. Do not claim a flat selected list establishes successful execution.
Identify missing evidence without inventing completion or measured speedups.
Older pins retain their contracts; analysis remains read-only.

## Workspace Docs 8 Execution Boundary

For a repository pinned to v8, retain the v7 lifecycle, review, approval, and
freshness rules while applying the v8 verification boundary: local checks cover
changed behavior and all affected direct/transitive consumers; skip unrelated
projects/suites. Complete required gates run in CI after the candidate stabilizes,
without a duplicate complete local run before requesting CI. Unknown impact
requires investigation and justified CI fallback; missing CI cannot prove final
acceptance. Work on one active task per agent. When writing a spec, split oversized
scope into bounded ordered steps with dependencies, acceptance mapping, and
focused validation; use linked child specs for independently managed delivery.
Preserve this skill's planning/read-only scope and explicit older-pin contracts.
