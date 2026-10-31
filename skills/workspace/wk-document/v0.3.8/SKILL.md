---
name: wk-document
description: Run the wk.document lifecycle facade to create or maintain human-facing project documentation within repository ownership boundaries. Invoke explicitly when documentation must be reconciled with current behavior and validated.
metadata:
  skm-version: "0.3.8"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3fae5b83a7a8324e871d7e707f1c73498b02bb1f"
  skm-source-path: "workspace/instructions/skills/wk-document"
  skm-source-integrity: "sha256:6417c51113e80a6375cb825c3eb4f4167e84ea16b474f47bc615b3d6ce3d5fce"
  workspace-toolkit-version: "0.13.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/maintain-project-docs@0.3.8"
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

## Workspace Docs 9 Affected CI

For a v9 pin, complete final verification means every required affected CI job,
not every project/job in the repository. Docs/spec-only changes run related jobs;
backend-only and frontend-only changes run their own jobs. Shared inputs include
all proven direct/transitive consumers. Use validated job selection and preserve
required status/protections, dependency stages, and this skill's authority.
Unknown scope needs investigation and a justified fallback. Do not restore a
blanket full-repository CI run for known narrow scope. Older pins retain their
contracts; publication checks remain separate from ordinary change validation.
