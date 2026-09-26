---
name: wk-analyze
description: Run the wk.analyze lifecycle facade to produce a read-only, evidence-backed repository assessment. Invoke explicitly when the user wants repository structure, stack, SDLC, policy, documentation, active-work, risk, and gap analysis.
metadata:
  skm-version: "0.2.2"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "fd9dc5cd6086d8b6c7a8a61b0a74436da2d2a5ee"
  skm-source-path: "workspace/instructions/skills/wk-analyze"
  skm-source-integrity: "sha256:6d10164f7e37cff5a16950c9c85128cdd6d428aeec67d6ca2adbaffbfae1b5ba"
  workspace-toolkit-version: "0.5.0"
  workspace-docs-compatibility: "6.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/analyze-repository@0.2.2"
---

# wk.analyze

Route the request through `analyze-repository`.

1. Require the focused dependency and stop with an actionable installation or
   compatibility error when it is unavailable.
2. Remain read-only and preserve the user's requested scope.
3. Let the focused workflow inspect repository-local evidence and distinguish
   facts, documented intent, inferences, and evidence gaps.
4. Report purpose, structure, stack, entrypoints, Workspace and spec state,
   delivery conventions, documentation and memory status, security-sensitive
   boundaries, risks, and recommended next actions.

Do not create a spec, edit documentation, install dependencies, or inspect
sibling projects while operating through this facade.
