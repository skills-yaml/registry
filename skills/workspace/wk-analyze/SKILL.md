---
name: wk-analyze
description: Run the wk.analyze lifecycle facade to produce a read-only, evidence-backed repository assessment. Invoke explicitly when the user wants repository structure, stack, SDLC, policy, documentation, active-work, risk, and gap analysis.
metadata:
  skm-version: "0.1.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "6dbdf01341a8ab5d572179462f1b460ff6259c51"
  skm-source-path: "workspace/instructions/skills/wk-analyze"
  skm-source-integrity: "sha256:6d10164f7e37cff5a16950c9c85128cdd6d428aeec67d6ca2adbaffbfae1b5ba"
  workspace-toolkit-version: "0.3.0"
  workspace-docs-compatibility: "5.x"
  minimum-skm-version: "0.4.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/analyze-repository@0.1.0"
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
