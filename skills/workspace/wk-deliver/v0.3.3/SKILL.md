---
name: wk-deliver
description: Run the wk.deliver lifecycle facade to implement, validate, review, remediate, and advance an approved development specification through the repository's authorized delivery workflow. Invoke explicitly for end-to-end delivery rather than read-only review.
metadata:
  skm-version: "0.3.3"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "e205b8c9e4f092adb9b20aaa129e644d858a25ca"
  skm-source-path: "workspace/instructions/skills/wk-deliver"
  skm-source-integrity: "sha256:7602b7dd38f47006a7b7ef25afcc73a6c3922fe8e73e6949069d6e247c9920ad"
  workspace-toolkit-version: "0.8.0"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.4.3, workspace/plan-implementation@0.4.3, workspace/implement-spec@0.4.3, workspace/review-changes@0.4.3, workspace/review-security@0.4.3, workspace/monitor-ci@0.4.3, workspace/fix-ci@0.4.3, workspace/address-review-feedback@0.4.3, workspace/coordinate-multi-agent-development@0.2.3"
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
