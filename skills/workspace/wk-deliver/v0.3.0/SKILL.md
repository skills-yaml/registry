---
name: wk-deliver
description: Run the wk.deliver lifecycle facade to implement, validate, review, remediate, and advance an approved development specification through the repository's authorized delivery workflow. Invoke explicitly for end-to-end delivery rather than read-only review.
metadata:
  skm-version: "0.3.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "bdedc37407589cce10ce4f4db4c5c15ab1c33dce"
  skm-source-path: "workspace/instructions/skills/wk-deliver"
  skm-source-integrity: "sha256:88510d88b85d278a56a6234a270395631c084f03ba9429d83c841eabf36fcea6"
  workspace-toolkit-version: "0.7.0"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.4.0, workspace/plan-implementation@0.4.0, workspace/implement-spec@0.4.0, workspace/review-changes@0.4.0, workspace/review-security@0.4.0, workspace/monitor-ci@0.4.0, workspace/fix-ci@0.4.0, workspace/address-review-feedback@0.4.0, workspace/coordinate-multi-agent-development@0.2.0"
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
3. Run affected gate modules during implementation and review fixes. Regenerate
   affected artifacts and reconcile documentation before final verification;
   unknown scope or freshness uses the aggregate fallback.
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
