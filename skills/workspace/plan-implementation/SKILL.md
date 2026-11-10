---
name: plan-implementation
description: Build an ordered, evidence-backed implementation plan from an approved development specification. Use when a feature, migration, or refactor has an active spec and needs dependency ordering, concrete file areas, validation strategy, compatibility handling, and completion gates before code changes begin.
metadata:
  skm-version: "0.6.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "4cd12dc61260ef1a5a3f5e114e0d2c8fb04d18ff"
  skm-source-path: "workspace/instructions/skills/plan-implementation"
  skm-source-integrity: "sha256:5f5664fa28895ec8ac2e482ebd2295b2979cd53ee8c580634f27e73211220831"
  workspace-toolkit-version: "0.16.0"
  workspace-docs-compatibility: "10.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/design-domain-model@0.2.0"
---

# Plan Implementation

Translate an active specification into executable work while keeping the plan
grounded in the current repository.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. Report unresolved conflicts
between current instruction files instead of planning from a conflicting copy.

## Plan the Work

1. Verify that the spec is in the locally required development state and has
   scope, acceptance criteria, affected areas, validation gates, and
   memory impact initialized as pending or resolved with a valid rationale.
2. Read the governing instructions and inspect the actual entrypoints, data
   flows, tests, and closest implementation precedents.
3. Identify dependencies, externally visible contracts, migration boundaries,
   collision risks, and the smallest safe delivery slices.
4. Resolve facts from the repository. Label assumptions and stop on missing
   decisions that would materially change behavior or data.

## Produce an Executable Plan

For each ordered step state:

- the outcome, not just the activity;
- the files or components likely to change;
- dependencies on earlier steps;
- changed-component tests/checks, then affected direct/transitive consumer stages
  gated on upstream success, with selection reasons and failure/coverage gaps;
- validation for success and representative failure cases;
- rollback, compatibility, or migration considerations;
- the acceptance criteria the step advances.

Design gate modules from actual inputs, dependencies, consumers, Taskfile
commands, resources, pass conditions, and freshness rules. Include affected
iteration gates, artifact generation, self-review and required independent
exact-candidate review, finding resolution, a frozen-candidate boundary, full
required gates, spec lifecycle reconciliation,
and memory-impact classification. Include ordinary commit, push, pull-request,
CI, test-integration, and non-destructive release steps under standing workflow
authority. Model scoped human approval for substantial scope expansion and destructive
production actions alongside governed instruction changes. When governed instructions are
affected, plan a prospective instruction-change approval gate before their
first edit. A direct human request naming the instruction outcome already
satisfies that gate; general standing authority and an agent-authored spec do
not.
Plan the lifecycle handoffs separately: local implementation remains in
development, confirmed integration into the configured test target moves the
spec to test, and the confirmed pinned completion event moves it to done
(verified main merge plus reconciled acceptance and records in v7). Use `develop`
and `main` only as defaults when local policy does not name equivalent targets.

Normal infrastructure management uses OpenTofu through Taskfile in CI/CD.
For a one-time user-run operation permitted by the actual pinned SDLC, plan the
spec, tools/ source, bounded targets, preview/failure/recovery checks, review and
affected CI before an exact approval/user-execution handoff. Agents never run
workstation mutations. Establish import support, configuration/resource address
and remote state ownership before manual infrastructure creation; require
OpenTofu import and a matching plan afterward. Include any approved human-run
state step in the exact sequence. Older pins retain their restrictions.

## Hand Off

Call out critical-path decisions, parallel-safe work, known risks, and any
acceptance criterion not covered by a planned validation. Persist the plan only
when requested or required by repository policy. Do not modify implementation
files while operating in a planning-only role.

## Domain and Schema Design Handoff

For model/schema changes, consume the evidence from $design-domain-model or
equivalent existing artifacts. Resolve material domain decisions before dependent
implementation; order invariant enforcement, storage/conversion changes, public
contracts and consumer migration by their actual dependencies. Preserve engine
policy and supported reader/writer versions. Select changed-component checks
first, then affected consumers; schema parsing alone cannot verify business rules
or data restoration. A small change can use a concise model delta.

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
