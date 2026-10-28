---
name: wk-document
description: Run the wk.document lifecycle facade to create or maintain human-facing project documentation within repository ownership boundaries. Invoke explicitly when documentation must be reconciled with current behavior and validated.
metadata:
  skm-version: "0.3.7"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "ea074843f54a3197ae9adf8ada2e770c0caa862c"
  skm-source-path: "workspace/instructions/skills/wk-document"
  skm-source-integrity: "sha256:dc187d63152465ae3cf8d78b03cfd2f34c2e645b7c5a4bbba060e2e4d4a843d6"
  workspace-toolkit-version: "0.12.0"
  workspace-docs-compatibility: "8.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/maintain-project-docs@0.3.7"
---

# wk.document

Route the request through `maintain-project-docs`.

1. Require the focused dependency and stop with an actionable installation or
   compatibility error when it is unavailable.
2. Confirm that the user's request authorizes the requested documentation
   writes; invocation alone is not write authority.
3. Let the focused workflow use current code, specs, and authoritative policy
   as evidence, update only declared human-facing documentation roots, reconcile
   affected references, and run repository-native gates.
4. Keep governed instructions out of scope unless the human request names that
   exact instruction change.
5. Report changed documents, validation, memory impact, and deferred gaps.

Do not turn documentation maintenance into an undocumented policy migration.

## Pinned Workflow Routing

Use affected documentation modules during edits. Let the focused workflow
resolve required review before freezing the candidate and running full final
gates. Reconcile the pinned lifecycle without claiming completion or publication
from documentation changes alone.

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
