---
name: wk-deliver
description: Run the wk.deliver lifecycle facade to implement, validate, review, remediate, and advance an approved development specification through the repository's authorized delivery workflow. Invoke explicitly for end-to-end delivery rather than read-only review.
metadata:
  skm-version: "0.4.4"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3fae5b83a7a8324e871d7e707f1c73498b02bb1f"
  skm-source-path: "workspace/instructions/skills/wk-deliver"
  skm-source-integrity: "sha256:be493dd50ea7678525fe5948eda54283da62083837d8e14bbc4e2c25f4130341"
  workspace-toolkit-version: "0.13.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.6.2, workspace/plan-implementation@0.5.4, workspace/implement-spec@0.5.4, workspace/review-changes@0.5.4, workspace/review-security@0.5.4, workspace/monitor-ci@0.4.8, workspace/fix-ci@0.4.8, workspace/address-review-feedback@0.4.8, workspace/coordinate-multi-agent-development@0.2.8"
---

# wk.deliver

Coordinate the declared specification, planning, implementation, review,
security, CI, and remediation dependencies. Invocation alone grants no write,
publication, instruction-change, production, or scope authority.

## Deliver

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
   stabilize, freeze the candidate and run `task check`, `task test`, and every
   applicable project gate. Reuse only proven-fresh evidence and verify actual
   combined integration/main revisions. Record evidence for each acceptance
   criterion; missing decisions or required failures block completion.
6. Use CI monitoring and bounded repair only within the repository's standing
   workflow authority. Never bypass protections or perform destructive
   production actions without the separately required human approval.
7. Advance a spec only on the pinned completion evidence, never from branch
   name alone. Under v7, verified main merge completes work after all records
   and memory are reconciled; publication remains separate. Older pins retain
   their completion contract. Run affected modules during iteration, resolve
   review findings, then run full final-candidate gates.

Report completed, deferred, and skipped work with reasons, validation evidence,
review disposition, lifecycle state, and rollback guidance. Later tracked
result/integration records require affected review and verification reconciliation;
reuse only proven-fresh evidence.

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
