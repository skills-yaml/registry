---
name: wk-plan
description: Run the wk.plan lifecycle facade to validate or create an active specification and produce an executable implementation plan. Invoke explicitly when approved work needs ordered steps, affected files, migration handling, validation, rollback, and completion gates.
metadata:
  skm-version: "0.4.4"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3fae5b83a7a8324e871d7e707f1c73498b02bb1f"
  skm-source-path: "workspace/instructions/skills/wk-plan"
  skm-source-integrity: "sha256:6000e0f9ce690ba61fff2ebf8c26876b925aa163469ad96bdcc4046a61f02dba"
  workspace-toolkit-version: "0.13.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.6.2, workspace/plan-implementation@0.5.4"
---

# wk.plan

Compose `write-spec` and `plan-implementation`.

1. Require both focused dependencies and stop with an actionable installation
   or compatibility error when either is unavailable.
2. Locate the active specification. If none adequately covers a user-requested
   plan, use `write-spec` first without starting implementation.
3. Stop when the spec is ambiguous, incomplete, not in an implementable state,
   lacks required authority, or conflicts with current authoritative
   instructions.
4. Otherwise use `plan-implementation` to produce dependency-ordered,
   reviewable steps with concrete affected areas, compatibility and migration
   handling, per-step validation, rollback, and completion gates.
5. Report assumptions, blockers, and the exact implementation handoff.

Do not edit product code or treat planning as authority to deliver changes.

## Pinned Workflow Routing

Have the focused plan declare module inputs, dependencies, consumers,
resources, freshness, review/finding resolution, and full final gates. Plan
changed-component checks first, then affected direct/transitive consumer stages
gated on upstream success, with selection reasons, fallback, and coverage gaps.
Under v7,
plan main completion separately from deployment/publication and include blocked
resume conditions where needed. Planning does not start deferred implementation.

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
