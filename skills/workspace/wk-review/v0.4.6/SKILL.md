---
name: wk-review
description: Run the wk.review lifecycle facade for a read-only correctness and applicable security review of a working tree, branch, commit range, or pull request. Invoke explicitly when findings and validation gaps are needed without remediation.
metadata:
  skm-version: "0.4.6"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "b3d3173635d9a8c2896f4d45a17bcdd41e6155a5"
  skm-source-path: "workspace/instructions/skills/wk-review"
  skm-source-integrity: "sha256:eef5f880e7cfbc923501d777ecd5f477538ee228d1da6840bbe05b64b1ccb36c"
  workspace-toolkit-version: "0.14.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/review-changes@0.5.6, workspace/review-security@0.6.0"
---

# wk.review

Compose `review-changes` and, when applicable, `review-security`.

1. Require both focused dependencies and stop with an actionable installation
   or compatibility error when either is unavailable.
2. Remain read-only. Confirm the exact review target and inspect its governing
   requirements plus relevant surrounding code.
3. Always use `review-changes`. Also use `review-security` when the change
   affects a trust boundary, authentication or authorization, identity,
   secrets, untrusted input, file or network access, supply chain, execution,
   tenant isolation, or sensitive data.
4. Combine duplicate evidence without hiding either review dimension.
5. Lead with actionable findings ordered by severity and include precise file
   and line evidence, then assumptions, validation gaps, and disposition.

Do not edit files, resolve review threads, publish artifacts, or remediate
findings unless the user separately requests and authorizes that work.

## Pinned Workflow Routing

Bind independent review to the exact candidate under the pinned risk rules.
For v7, allow final full gates to remain pending until findings are resolved;
assess main-completion and blocked-state claims separately from publication.
Assess changed-component checks preceding affected direct/transitive consumer
checks, selection reasons, coverage gaps, and proven freshness; a flat selection
is not passing evidence. Relevant edits renew review. Remain read-only.

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
