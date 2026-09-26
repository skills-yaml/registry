---
name: wk-review
description: Run the wk.review lifecycle facade for a read-only correctness and applicable security review of a working tree, branch, commit range, or pull request. Invoke explicitly when findings and validation gaps are needed without remediation.
metadata:
  skm-version: "0.2.2"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "fd9dc5cd6086d8b6c7a8a61b0a74436da2d2a5ee"
  skm-source-path: "workspace/instructions/skills/wk-review"
  skm-source-integrity: "sha256:0a11deca7a56d348f398b6a43c540efead71d26fb8b06db51a685b416f24d4c4"
  workspace-toolkit-version: "0.5.0"
  workspace-docs-compatibility: "6.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/review-changes@0.3.2, workspace/review-security@0.3.2"
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
