---
name: wk-review
description: Run the wk.review lifecycle facade for a read-only correctness and applicable security review of a working tree, branch, commit range, or pull request. Invoke explicitly when findings and validation gaps are needed without remediation.
metadata:
  skm-version: "0.4.3"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "ea074843f54a3197ae9adf8ada2e770c0caa862c"
  skm-source-path: "workspace/instructions/skills/wk-review"
  skm-source-integrity: "sha256:2d41bb99ebbdca88199c806ecd42a46f0c18e2f2a018e8e2e58ff28466937efc"
  workspace-toolkit-version: "0.12.0"
  workspace-docs-compatibility: "8.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/review-changes@0.5.3, workspace/review-security@0.5.3"
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
