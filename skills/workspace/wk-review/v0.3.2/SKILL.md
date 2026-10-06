---
name: wk-review
description: Run the wk.review lifecycle facade for a read-only correctness and applicable security review of a working tree, branch, commit range, or pull request. Invoke explicitly when findings and validation gaps are needed without remediation.
metadata:
  skm-version: "0.3.2"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3bf955b7b41193e3e124e4b62757b71eac46228e"
  skm-source-path: "workspace/instructions/skills/wk-review"
  skm-source-integrity: "sha256:f6ef8d7745fc56fe60e8ea1073a79a0205ce3f98500ace40ce1b11768330a483"
  workspace-toolkit-version: "0.7.2"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/review-changes@0.4.2, workspace/review-security@0.4.2"
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
