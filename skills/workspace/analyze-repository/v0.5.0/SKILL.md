---
name: analyze-repository
description: Analyze a repository without modifying it, producing an evidence-backed account of its purpose, structure, technology stack, development lifecycle, policies, documentation state, active work, risks, and evidence gaps. Use when a repository needs assessment, onboarding context, or current-state discovery before planning work.
metadata:
  skm-version: "0.5.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "4cd12dc61260ef1a5a3f5e114e0d2c8fb04d18ff"
  skm-source-path: "workspace/instructions/skills/analyze-repository"
  skm-source-integrity: "sha256:7a3dabb059bb31b92e67ae0396e57903253e648d36050fd66c5279b373cea6c1"
  workspace-toolkit-version: "0.16.0"
  workspace-docs-compatibility: "10.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/design-domain-model@0.2.0"
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

Every analysis follows the [analysis report template](templates/analysis-report.md)
exactly so different agents give comparably shaped answers. Keep its sections,
summary labels, table columns, order and controlled vocabulary; use its empty,
out-of-scope and `unknown` markers and emit none of its comment guidance.

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
and freshness justify affected iteration and the pinned final coverage after review.
Assess staged development evidence: changed-component checks must pass before
checks of affected direct/transitive consumers in dependency order. Inspect
contract and side-effect impact, missing coverage/tools, fallback reasons,
old/new dependencies for renames/deletions, overlapping changes, cycles, and
freshness. Do not claim a flat selected list establishes successful execution.
Identify missing evidence without inventing completion or measured speedups.
Older pins retain their contracts; analysis remains read-only.

## Pinned SDLC Contract

Read the repository's pinned SDLC; this skill does not override its authority
or this skill's read-only/planning boundary. Deliver the requested scope using
existing patterns. Report optional improvements separately and leave them
unimplemented. Before substantial scope expansion, identify the concrete
blocker, propose the smallest solution and obtain approval. Standing workflow
authority never grants unrelated work or governed instruction changes.

For v7 and later, ordinary task branches and safe delivery follow task authority.
Done means verified main merge with acceptance, documentation, catalog, versions
and memory reconciled; publication is separate. Preserve done history with
linked follow-ups. Blocked work records previous stage, kind, reason and resume
condition; resume that stage with renewed evidence. Shared test integration is
the default; a documented direct route preserves the same gates.

Security, data integrity, public interfaces, governed instructions and release
controls require independent exact-candidate review. Other non-trivial changes
require it except small low-risk changes with focused tests. Resolve findings
by a fix or reviewer-agreed documented rejection; optional suggestions remain
outside scope. Finish relevant review, fixes, artifacts and knowable records
before final verification. Later edits renew affected evidence. Verify actual
combined integration/main revisions, record acceptance evidence and preserve
host protections; missing coverage/tools are gaps, never a pass.

Use the verification contract for the actual pin:

- v9 and later: changed behavior and all affected direct/transitive consumers locally;
  every required affected CI job on the stable candidate. Docs/spec, backend
  and frontend changes skip unrelated jobs. Preserve required status names,
  validated selection and dependency stages. No blanket full-repository run.
- v8: the same affected local boundary, then complete required gates in CI.
  Neither v8 nor v9/v10 requires a duplicate full local run before CI. Missing CI
  cannot establish final acceptance; unknown impact needs investigation and
  justified CI fallback.
- v7: affected modules during iteration, then full required final-candidate
  checks/tests after review and fixes. Earlier pins retain their own contract.

During development and review fixes, pass changed-component checks before
consumer checks in dependency order. Include interfaces, errors, security,
timing, side effects, configuration, dependencies and generated outputs in
impact analysis. Failures block dependent stages; deduplicate checks, assess
old/new relationships for moves/deletions and group cycles. Reuse only proven-
fresh evidence. Read-only work assesses this evidence; planning specifies it.
Work on one active task per agent. Split oversized specs into bounded ordered
steps with prerequisites, acceptance mapping and focused validation; use linked
child specs for independently deliverable work and preserve overall acceptance.
