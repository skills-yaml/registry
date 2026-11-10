---
name: maintain-project-docs
description: Create, update, reconcile, or review human-facing project documentation within repository-declared documentation roots. Use when project reference, architecture, operational, onboarding, or work documentation must reflect current repository behavior without changing governed agent instructions.
metadata:
  skm-version: "0.3.13"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "4cd12dc61260ef1a5a3f5e114e0d2c8fb04d18ff"
  skm-source-path: "workspace/instructions/skills/maintain-project-docs"
  skm-source-integrity: "sha256:90cafe839afb6fc0ab907edf07d296cbeb8e4d469ec30087d8b798a99d6f4841"
  workspace-toolkit-version: "0.16.0"
  workspace-docs-compatibility: "10.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Maintain Project Documentation

Keep project documentation accurate, connected, and within its declared
ownership boundary.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. Governed instruction changes
require prospective human instruction-change approval for the named scope.

## Establish Authority and Sources

1. Read repository policy, documentation ownership rules, nearby documents,
   relevant implementation, and active specifications.
2. Determine whether the request is documentation-only or follows an
   implementation change. Treat current behavior and authoritative instructions
   as evidence; report conflicts instead of copying stale text.
3. Write only within human-facing documentation roots declared by the
   repository. Do not edit root agent policy, design tokens, or files under
   `workspace/instructions/` unless the human request explicitly names that
   governed instruction scope.

If two or more agents may mutate the repository concurrently, invoke
`coordinate-multi-agent-development` before delegated edits. Give each
mutating agent a dedicated detached worktree and repository WIP record; keep
the primary checkout coordination-only. Ordinary task or delivery branches follow task authority under Workspace Docs 7;
older pins retain their direct branch-request requirement. Always honor protections.

## Maintain the Documentation

- Use the repository's established structure, terminology, and link style.
- Prefer links to authoritative policies over duplicated procedural text.
- Describe only the current project and use repository-relative paths in
  committed content.
- Keep examples safe, deterministic, and free of secrets or machine-local
  information.
- Reconcile affected indexes, navigation, diagrams, and nearby references when
  the requested change makes them stale.
- Preserve manual content and unrelated work.

## Validate and Hand Off

Run affected documentation modules during edits. Review factual accuracy,
links, policy consistency, and local-information boundaries. Classify and record
knowable memory impact under local policy and reconcile spec/catalog records
before required independent exact-candidate review. Resolve findings and
stabilize records/documentation before freezing the candidate and running full
required gates. Reuse only proven-fresh evidence. Report final results at handoff;
later tracked result or integration records require affected review and gate
reconciliation. Include changed documents and any known or deferred gap.

After the user requests the documentation change, standing workflow authority
covers its ordinary edits, validation, commits, pull-request updates, CI work,
and non-destructive release steps. Ordinary branch creation and pushing follow the pinned SDLC authority. Pause for an unapproved
governed instruction change, a destructive production action, or a material
missing product decision.

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
