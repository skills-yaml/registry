---
name: write-spec
description: Turn an accepted problem or feature request into a lifecycle-managed development specification. Use when work needs explicit scope, acceptance criteria, affected areas, validation gates, risks, migration considerations, and memory impact before implementation begins.
metadata:
  skm-version: "0.6.2"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3fae5b83a7a8324e871d7e707f1c73498b02bb1f"
  skm-source-path: "workspace/instructions/skills/write-spec"
  skm-source-integrity: "sha256:dac25a4f4cff707b89525136e00c3a57269a3b86459562ca8f931f9c903c5dba"
  workspace-toolkit-version: "0.13.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/design-domain-model@0.1.4"
---

# Write Spec

Create a decision-ready specification without starting implementation.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. A spec records or proposes
policy but cannot override a current governed instruction.

## Establish the Contract

1. Read repository policy, the root spec catalog, the nearest related specs,
   and relevant architecture or product documentation.
2. Confirm the problem, desired outcome, constraints, and explicit exclusions.
   Identify what is missing, ambiguous, or contradictory (see Resolve Missing
   or Unclear Information) and ask the user before writing the spec.
3. Select the lifecycle state and primary-feature category required by local
   policy. Reuse an existing category when it accurately describes the work.
   For Workspace Docs 7, use `backlog`, `development`, `test`, `done`, or
   `blocked`. Default to shared-test integration; a documented direct-to-main
   route preserves every gate. Blocked specs record Previous State, Block Kind,
   Block Reason, and Resume Condition. Older pins retain their original states
   and transition requirements.
4. Preserve unrelated work and existing decisions. Mark assumptions and open
   questions instead of presenting them as settled facts.

If two or more agents may mutate the repository concurrently, invoke
`coordinate-multi-agent-development` before delegated edits. Give each
mutating agent a dedicated detached worktree and repository WIP record; keep
the primary checkout coordination-only. Ordinary task or delivery branches follow task authority under Workspace Docs 7;
older pins retain their direct branch-request requirement. Always honor protections.

## Resolve Missing or Unclear Information

Before writing, check the request against the required spec contents below.
When information needed for scope, goals and non-goals, users or consumers,
behavior or interface contracts, affected areas, acceptance criteria, risks,
version impact, or approval scope is missing, vague, or conflicting and
repository evidence does not settle it, ask the user instead of guessing.

- Ask a small focused batch of specific questions in plain language, each with
  the options or default you would otherwise assume. Use the host's question
  tool when one is available, and wait for the actual answers before dependent
  writing; silence is not a choice.
- Do not ask what the request, repository, catalog, memory, or prior answers
  already establish, and do not ask for routine delivery permission.
- Continue read-only discovery while waiting. If an answer cannot be obtained,
  record it as a labeled open question or assumption in the spec and do not
  present it as settled; never invent requirements, versions, or approvals.

## Write the Specification

Include at least:

- lifecycle state and a concise status rationale;
- problem, goals, non-goals, and users or consumers;
- proposed behavior and important interface or data contracts;
- affected areas and compatibility or migration effects;
- security, privacy, reliability, and rollback risks where applicable;
- measurable acceptance criteria;
- required validation gates, changed-component checks, and subsequent affected
  direct/transitive consumer stages, including selection reasons and gaps;
- ordered, task-sized delivery steps when the scope cannot be completed safely
  in one focused change (see Break Large Specs into Focused Steps);
- a `Memory Impact` section using the repository's required initial status.

When affected areas include governed instructions, add an Instruction Change
Approval section that records whether prospective human approval is pending or
was directly supplied and its exact scope. The record supports auditability but
is not itself approval: an agent-authored spec cannot grant instruction-change
approval. Do not modify governed instructions while approval is pending.

For infrastructure scope, make OpenTofu the only implementation and state
management mechanism. Reject acceptance paths that depend on consoles,
provider mutation CLIs, alternative IaC engines, or ad hoc provisioning scripts.
Require local development to remain non-mutating: contributors may change
OpenTofu configuration and run validation or review locally, but applies,
destroys, imports, and state mutations must run only through the repository's
CI/CD workflow. CI/CD does not authorize provider CLI writes.

Use normative language only for real requirements. Keep implementation details
out unless they constrain compatibility, safety, or acceptance.

## Break Large Specs into Focused Steps

Before finalizing a new or revised spec, assess whether its scope can be
implemented, reviewed, and validated as one focused change. Split it when it
combines distinct deliverables, dependency stages, migrations, or risk areas
that need separate acceptance evidence. Use those boundaries rather than page
length, a fixed step count, or an arbitrary time estimate. Keep small specs
concise; do not split tightly coupled invariants into unsafe intermediate states.

For oversized scope, write ordered steps with stable IDs. Each step MUST define:

- one concrete outcome and bounded affected areas, including exclusions;
- prerequisites and dependencies on earlier steps or unresolved decisions;
- measurable acceptance criteria mapped to the spec's overall criteria;
- the smallest meaningful changed-component checks and affected-consumer checks,
  with selection reasons and required evidence for completion.

Split a step again if it still contains multiple independently reviewable tasks.
Plan one ready step at a time per agent. Require passing acceptance evidence
before dependent steps begin; unresolved decisions block dependent work without
inventing answers or preventing established independent steps from being planned.
Do not add unrelated edits or tests to a step. Preserve cross-step contracts,
compatibility, migration/rollback safety, integration checks, and mandatory final
repository gates; passing isolated steps does not prove the complete feature.

Keep steps in one spec when they share one delivery and lifecycle. When parts
need independent delivery or lifecycle tracking, create linked child specs:
the parent records the overall outcome, dependencies, and acceptance mapping;
each child links back and follows the repository's feature, catalog, lifecycle,
version, approval, and memory requirements. Do not mark the parent complete
until its overall acceptance and pinned completion requirements are met.
Preserve completed specs and create linked follow-ups for later decomposition.
This remains planning work and does not authorize implementation.

## Integrate and Review

1. Put the spec in the required lifecycle and primary-feature path.
2. Update the root spec catalog in the same change, including current state and
   why the spec is in that state.
   For `test` and `done`, cite confirmed integration and the pinned completion event; do
   not infer delivery from the checked-out branch name alone.
3. Check links, terminology, category placement, acceptance testability, and
   consistency with existing policy.
4. Self-review and obtain independent exact-candidate review where the pinned
   risk rules require it. Resolve every finding before freezing the candidate
   and running the required final documentation, spec, and aggregate gates.
5. Hand off the unresolved decisions and the next allowed lifecycle transition.
   Use the documented test target, conventionally `develop`. Under v7, verified
   main merge completes work after acceptance and records are reconciled;
   deployment and publication are separate. Preserve done history with linked
   follow-up specs. Do not infer completion from a branch name.

Do not implement the feature while operating in this planning role. A requested
specification workflow may use standing authority to commit, push its delivery
branch, and create or update a pull request. Advance lifecycle only when the
required delivery evidence exists. Require scoped human approval only for a
destructive production action outside the governed instruction-change
exception described above.

## Version Impact

Before implementation, include the per-component Version Impact table required
by the pinned standard and register member specs in `workspace/releases.json`.
Classify major, minor, patch, or justified none; declare a shared reservation
with baseline, target, owner, timing, and rationale. Check occupied versions
before proposing a target. Do not apply a development bump to a backlog idea.

## Domain and Schema Design

When requirements change business concepts, lifecycle/invariants, data ownership
or database/API/event contracts, use $design-domain-model in design mode to
produce or reuse proportionate modeling evidence. Carry scenario/invariant IDs,
representation mappings, affected consumers and material questions into the spec.
A clear field/CRUD change needs a model delta, not a mandatory DDD workshop.
Keep unresolved material business rules explicit; planning does not authorize
application/schema implementation.

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
