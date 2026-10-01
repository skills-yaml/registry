---
name: wk-analyze
description: Run the wk.analyze lifecycle facade to produce a read-only, evidence-backed repository assessment. Invoke explicitly when the user wants repository structure, stack, SDLC, policy, documentation, active-work, risk, and gap analysis.
metadata:
  skm-version: "0.3.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "bdedc37407589cce10ce4f4db4c5c15ab1c33dce"
  skm-source-path: "workspace/instructions/skills/wk-analyze"
  skm-source-integrity: "sha256:681e4b5517deb9ac97cd3d843f252e415e3de5cbf97c6b670131b2759aab845b"
  workspace-toolkit-version: "0.7.0"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/analyze-repository@0.3.0"
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

## Pinned Workflow Routing

Have the focused read-only analysis distinguish v7 main completion, separate
publication, blocked/resume evidence, and modular-gate freshness. Do not turn
assessment into lifecycle mutation; older pins retain their contracts.
