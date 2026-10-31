---
name: wk-spec
description: Run the wk.spec lifecycle facade to turn an accepted request into a complete, categorized, lifecycle-managed development specification. Invoke explicitly when implementation needs scope, acceptance criteria, affected areas, validation, risks, and memory impact.
metadata:
  skm-version: "0.4.4"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3fae5b83a7a8324e871d7e707f1c73498b02bb1f"
  skm-source-path: "workspace/instructions/skills/wk-spec"
  skm-source-integrity: "sha256:82c213c04ebaa639aa8459b1bdb32247106cbb9819a789be4f023181be098be3"
  workspace-toolkit-version: "0.13.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.6.2"
---

# wk.spec

Route the request through `write-spec`.

1. Require the focused dependency and stop with an actionable installation or
   compatibility error when it is unavailable.
2. Preserve the user's accepted problem and use repository evidence. Ask the
   user, through the focused workflow, about missing, unclear, or conflicting
   information that the evidence cannot settle; do not guess requirements.
3. Let the focused workflow detect conflicts with authoritative instructions,
   select the single valid feature and lifecycle path, write the complete spec,
   break oversized scope into ordered, task-sized steps or linked child specs,
   update its canonical catalog, and run repository-native gates.
4. Record governed-instruction approval status accurately. A spec cannot grant
   that approval.
5. Report unresolved decisions and the next allowed transition without starting
   implementation.

Do not duplicate the focused skill's specification template or lifecycle rules.

## Pinned Workflow Routing

Have validation criteria specify changed-component checks followed by affected
direct/transitive consumer stages gated on success, with selection reasons and
coverage gaps. Preserve full final verification and planning-only boundaries.

Use the pinned states and completion definition through write-spec. For v7,
include blocked metadata when applicable, preserve done history with linked
follow-ups, and plan independent review before full final verification. Keep
specification work separate from implementation.

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
