---
name: analyze-repository
description: Analyze a repository without modifying it, producing an evidence-backed account of its purpose, structure, technology stack, development lifecycle, policies, documentation state, active work, risks, and evidence gaps. Use when a repository needs assessment, onboarding context, or current-state discovery before planning work.
metadata:
  skm-version: "0.4.4"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3fae5b83a7a8324e871d7e707f1c73498b02bb1f"
  skm-source-path: "workspace/instructions/skills/analyze-repository"
  skm-source-integrity: "sha256:6ddd0925dcd0f201dd629f62db0a1cc6a8a979df5033d81301ea7d7db6cd3bf1"
  workspace-toolkit-version: "0.13.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/design-domain-model@0.1.4"
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

## Workspace Docs 9 Affected CI

For a v9 pin, complete final verification means every required affected CI job,
not every project/job in the repository. Docs/spec-only changes run related jobs;
backend-only and frontend-only changes run their own jobs. Shared inputs include
all proven direct/transitive consumers. Use validated job selection and preserve
required status/protections, dependency stages, and this skill's authority.
Unknown scope needs investigation and a justified fallback. Do not restore a
blanket full-repository CI run for known narrow scope. Older pins retain their
contracts; publication checks remain separate from ordinary change validation.
