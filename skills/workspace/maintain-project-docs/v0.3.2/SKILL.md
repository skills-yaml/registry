---
name: maintain-project-docs
description: Create, update, reconcile, or review human-facing project documentation within repository-declared documentation roots. Use when project reference, architecture, operational, onboarding, or work documentation must reflect current repository behavior without changing governed agent instructions.
metadata:
  skm-version: "0.3.2"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3bf955b7b41193e3e124e4b62757b71eac46228e"
  skm-source-path: "workspace/instructions/skills/maintain-project-docs"
  skm-source-integrity: "sha256:8c70dcc68c53c6267c38c71421c18407286a5e43a35c94f39539c18b5f53ba09"
  workspace-toolkit-version: "0.7.2"
  workspace-docs-compatibility: "7.x"
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

Read the project's pinned SDLC before planning or delivery. For Workspace Docs
7, done means verified merge into main with reconciled acceptance, documentation,
catalog, version records, and memory; deployment/publication is separate.
Blocked records previous stage, kind, reason, and resume condition; resume there
and renew stale evidence. Preserve done history with linked follow-up specs.
Shared test integration is the default; only an explicitly documented direct
route may omit it, preserving all gates. Older pins keep their prior completion
and branch-authority contracts.

For v7, the task request authorizes ordinary task branches and safe delivery.
Security, data integrity, public interfaces, governed instructions, and release
controls always require independent exact-candidate review; other non-trivial
changes require it except small low-risk changes with focused tests.
Resolve every finding by implementation or reviewer-agreed documented rejection.
For v7 development and review fixes, map changed behavior and direct/transitive
consumers, including interfaces, errors, security, timing, side effects,
configuration, dependencies, and generated outputs. Run the smallest meaningful
changed-component tests/checks first; only after they pass, run affected consumer
checks in dependency order through the transitive chain. Failure blocks dependent
stages; missing coverage or tools is a gap, never a pass. Deduplicate overlapping
checks, assess old/new relationships for deletions and renames, and group cycles.
Avoid unrelated aggregate runs; unknown impact requires justified safe fallback.
Keep required contract/integration/end-to-end coverage and native CI protections.
Reuse only proven-fresh evidence after further edits; a flat selection is not
execution order. Read-only skills assess evidence without mutating; planning
skills specify stages without implementing. Reconcile
knowable spec, catalog, and memory records before required review. Finish review,
artifacts, documentation, records, and fixes before freezing the candidate and
running full required checks/tests. Later tracked event/result records renew
affected review and verification; they do not automatically preserve evidence. Reuse only proven-fresh evidence and verify actual
combined integration/main revisions. Each acceptance criterion needs supporting
evidence; subjective product decisions go to the user. Read-only skills remain
read-only and planning skills do not implement changes.
