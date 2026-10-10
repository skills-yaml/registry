---
name: analyze-repository
description: Analyze a repository without modifying it, producing an evidence-backed account of its purpose, structure, technology stack, development lifecycle, policies, documentation state, active work, risks, and evidence gaps. Use when a repository needs assessment, onboarding context, or current-state discovery before planning work.
metadata:
  skm-version: "0.4.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "76bbf51eeb27c663755d5494649b2a2b8b5dd0c5"
  skm-source-path: "workspace/instructions/skills/analyze-repository"
  skm-source-integrity: "sha256:befc8cd24da5fffed829dd5ebda8dab3dd6fc15389e7e04819b062119c839036"
  workspace-toolkit-version: "0.9.0"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/design-domain-model@0.1.0"
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
