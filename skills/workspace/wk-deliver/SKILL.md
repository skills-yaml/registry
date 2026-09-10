---
name: wk-deliver
description: Run the wk.deliver lifecycle facade to implement, validate, review, remediate, and advance an approved development specification through the repository's authorized delivery workflow. Invoke explicitly for end-to-end delivery rather than read-only review.
metadata:
  skm-version: "0.1.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "6dbdf01341a8ab5d572179462f1b460ff6259c51"
  skm-source-path: "workspace/instructions/skills/wk-deliver"
  skm-source-integrity: "sha256:39d4795350f44be0c5a403367a429c0a8461fddc2e7bb9ce18aad2580609885f"
  workspace-toolkit-version: "0.3.0"
  workspace-docs-compatibility: "5.x"
  minimum-skm-version: "0.4.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.2.0, workspace/plan-implementation@0.2.0, workspace/implement-spec@0.2.0, workspace/review-changes@0.2.0, workspace/review-security@0.2.0, workspace/monitor-ci@0.2.0, workspace/fix-ci@0.2.0, workspace/address-review-feedback@0.2.0"
---

# wk.deliver

Coordinate the declared specification, planning, implementation, review,
security, CI, and remediation dependencies. Invocation alone grants no write,
publication, instruction-change, production, or scope authority.

## Deliver

1. Verify the active spec, catalog, human authority, repository state, and
   implementation plan. Use `write-spec` or `plan-implementation` only when the
   user's delivery request authorizes filling those prerequisites. Stop for an
   irreducible product decision or an unapproved governed instruction change.
2. Use `implement-spec` to divide the plan into reviewable steps. After each
   step, validate its acceptance criteria and close detected gaps before
   continuing.
3. Run all repository-required aggregate checks and tests.
4. Use `review-changes` for an independent correctness review. Use
   `review-security` when authentication, authorization, identity, sessions,
   tokens, tenant boundaries, secrets, untrusted input, file or network access,
   supply chain, execution boundaries, or sensitive data are affected.
5. Use the applicable remediation skills for in-scope findings, rerun affected
   gates, and re-review material changes. Completion requires no unresolved
   correctness finding, applicable security finding, failed required gate, or
   unmet acceptance criterion.
6. Use CI monitoring and bounded repair only within the repository's standing
   workflow authority. Never bypass protections or perform destructive
   production actions without the separately required human approval.
7. Advance a spec only on confirmed integration or release evidence, never
   from branch name alone. Resolve memory impact before a completed release.

Report completed, deferred, and skipped work with reasons, validation evidence,
review disposition, lifecycle state, and rollback guidance.
