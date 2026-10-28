---
name: wk-analyze
description: Run the wk.analyze lifecycle facade to produce a read-only, evidence-backed repository assessment. Invoke explicitly when the user wants repository structure, stack, SDLC, policy, documentation, active-work, risk, and gap analysis.
metadata:
  skm-version: "0.4.3"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "ea074843f54a3197ae9adf8ada2e770c0caa862c"
  skm-source-path: "workspace/instructions/skills/wk-analyze"
  skm-source-integrity: "sha256:8c7a584ca245e20cd37cdfb25e93c034dfed0ecc9dd3b511386268e410fc48f2"
  workspace-toolkit-version: "0.12.0"
  workspace-docs-compatibility: "8.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/analyze-repository@0.4.3"
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
publication, blocked/resume evidence, and modular-gate freshness. Assess staged
changed-component and affected direct/transitive consumer evidence, selection
reasons, and coverage gaps. Do not turn assessment into lifecycle mutation;
older pins retain their contracts.

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
