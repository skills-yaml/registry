---
name: wk-deliver
description: Deliver an approved specification or release already tested work through the repository's established workflow. Use for end-to-end delivery, release, promotion or resumption; preserve the requested scope and existing pipeline.
metadata:
  skm-version: "0.4.6"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "b3d3173635d9a8c2896f4d45a17bcdd41e6155a5"
  skm-source-path: "workspace/instructions/skills/wk-deliver"
  skm-source-integrity: "sha256:9f486a92027405ed29e7d2e6f90ae6f0185505c9b215dbbc6777de6b55d14645"
  workspace-toolkit-version: "0.14.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.6.4, workspace/plan-implementation@0.5.6, workspace/implement-spec@0.5.6, workspace/review-changes@0.5.6, workspace/review-security@0.6.0, workspace/monitor-ci@0.4.10, workspace/fix-ci@0.4.10, workspace/address-review-feedback@0.4.10, workspace/coordinate-multi-agent-development@0.2.10"
---

# wk.deliver

Coordinate the declared specification, planning, implementation, review,
security, CI, and remediation dependencies. Invocation alone grants no write,
publication, instruction-change, production, or scope authority.

## Release or Resume Tested Work

Choose this route when the requested outcome is release/promotion and the work
is already integrated in test or merged in main. Do not restart implementation
or reopen a done spec. Use existing release records, or a bounded follow-up only
when required for remaining release work.

1. Identify the requested outcome, exact tested revision/artifact, target
   environment, remaining operation and existing Taskfile/workflow. Read the
   repository instructions and handoff; confirm actual state, not branch names.
2. Check required acceptance, artifact provenance, review, CI and environment
   protections. Reuse only proven-fresh evidence; run only affected or required
   release checks. Missing evidence remains a gap to resolve through that path.
3. Execute the established release operation within standing workflow authority.
   Verify the deployed artifact/application and the requested observable behavior
   using existing health/smoke checks. Configuration written, applied changes,
   application running and behavior verified are distinct milestones.
4. If an operation fails, capture the failing command/run and relevant error.
   Use `fix-ci` only for a demonstrated blocker whose smallest repair fits the
   existing patterns and requested outcome. Validate affected behavior and
   consumers, then resume the same release. Never weaken a gate or protection.
5. A missing production pipeline, new workflow/infrastructure or architectural
   redesign is a substantial scope expansion: describe the concrete blocker
   and smallest proposal and obtain approval before implementing it. Report
   optional improvements separately and leave them unimplemented.

After interruption, restore the same artifact, environment, approved scope and
remaining operation from the handoff. Renew stale evidence without inventing
new delivery work. Preserve governed-instruction, OpenTofu, protected-credential
and destructive-production boundaries. Report the actual release status and
unverified behavior explicitly; a merge or workflow dispatch is not deployment.
Run OpenTofu mutations only through CI/CD and existing Taskfile entrypoints;
local infrastructure work is source-only and non-mutating. Provider CLI writes
remain forbidden in every environment.

## Implement Remaining Development Scope

1. Verify the active spec, catalog, human authority, repository state, and
   implementation plan. A blocked spec must resume at its recorded previous
   stage after its resume condition is satisfied; renew stale evidence before
   implementing. Use `write-spec` or `plan-implementation` only when the
   user's delivery request authorizes filling those prerequisites. Stop for an
   irreducible product decision or an unapproved governed instruction change.
2. Use `implement-spec` for remaining implementation only in active development.
   For an integrated test-stage spec, validate remaining acceptance at that
   stage rather than silently restarting implementation. Validate each step's
   criteria and close detected gaps before continuing. Reconcile knowable spec,
   catalog, documentation, and memory records before final review and freeze.
3. During implementation and review fixes, pass the smallest meaningful checks
   for changed behavior first, then verify affected direct/transitive consumers
   in dependency order. Failures block dependent stages; record selection reasons
   and gaps. Regenerate affected artifacts and reconcile documentation before
   final verification; unknown impact/freshness uses justified aggregate fallback.
4. Use `review-changes` for an independent exact-candidate correctness review. Use
   `review-security` when authentication, authorization, identity, sessions,
   tokens, tenant boundaries, secrets, untrusted input, file or network access,
   supply chain, execution boundaries, or sensitive data are affected.
5. Use remediation skills for in-scope findings, rerun affected modules, and
   renew affected review. Resolve every finding by a fix or reviewer-agreed
   documented rejection. Once review, fixes, artifacts, and documentation
   stabilize, freeze the candidate and run the final gates required by the
   actual pin below. Reuse only proven-fresh evidence and verify actual
   combined integration/main revisions. Record evidence for each acceptance
   criterion; missing decisions or required failures block completion.
6. Use CI monitoring and bounded repair only within the repository's standing
   workflow authority. Never bypass protections or perform destructive
   production actions without the separately required human approval.
7. Advance a spec only on the pinned completion evidence, never from branch
   name alone. Under v7, verified main merge completes work after all records
   and memory are reconciled; publication remains separate. Older pins retain
   their completion contract. Run affected modules during iteration, resolve
   review findings, then run the pinned final-candidate gates.

Report completed, deferred, and skipped work with reasons, validation evidence,
review disposition, lifecycle state, and rollback guidance. Later tracked
result/integration records require affected review and verification reconciliation;
reuse only proven-fresh evidence.

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

- v9: changed behavior and all affected direct/transitive consumers locally;
  every required affected CI job on the stable candidate. Docs/spec, backend
  and frontend changes skip unrelated jobs. Preserve required status names,
  validated selection and dependency stages. No blanket full-repository run.
- v8: the same affected local boundary, then complete required gates in CI.
  Neither v8 nor v9 requires a duplicate full local run before CI. Missing CI
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
