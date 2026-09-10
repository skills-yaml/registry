---
name: fix-bug
description: Reproduce, isolate, and fix a reported software defect with regression coverage. Use when observed behavior differs from a requirement or established contract and the user authorizes a focused implementation change.
metadata:
  skm-version: "0.2.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "6dbdf01341a8ab5d572179462f1b460ff6259c51"
  skm-source-path: "workspace/instructions/skills/fix-bug"
  skm-source-integrity: "sha256:1c5020566f1c2577773174330ada1c92f5e1cdaedf908a4ca1180a8d8c9635a8"
  workspace-toolkit-version: "0.3.0"
  workspace-docs-compatibility: "5.x"
  minimum-skm-version: "0.4.0"
  skm-adapter-compatibility: "2.x"
---

# Fix Bug

Correct the root cause while preserving unrelated behavior.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. Report unresolved conflicts
between current instruction files rather than guessing.

## Reproduce and Isolate

1. Read repository policy, the relevant spec or contract, and the bug report.
2. Establish expected versus actual behavior, affected versions or inputs, and
   a deterministic reproduction when practical.
3. Trace the smallest relevant execution path and identify the root cause.
   Distinguish it from symptoms, environmental failures, and nearby issues.
4. Inspect branch and worktree state and preserve unrelated user changes.

Treat governed instructions as read-only unless a direct human request
prospectively grants instruction-change approval for the named outcome or
scope. A general bug-fix request and standing workflow authority do not include
that permission. Do not edit governed instructions and seek approval
retroactively.

## Fix and Prove

1. Add a regression test that fails for the confirmed defect where feasible.
2. Implement the smallest coherent correction using established patterns.
3. Test boundary inputs, error paths, compatibility, and adjacent behavior.
4. Run focused checks followed by all required repository gates.
5. Self-review the complete diff against the reproduction and expected contract.
6. Reconcile the active spec, root catalog, and memory impact when local policy
   requires them. Keep the spec in development until confirmed test-target
   integration, then move it to test; move it to done only after confirmed
   production release.

For infrastructure defects, change OpenTofu configuration and run non-mutating
validation locally. Apply, destroy, import, and state correction must run only
through the repository's CI/CD Taskfile workflow. Any proposed local, direct,
provider-CLI, or alternative-engine mutation path is a blocker, not a fallback.

Report the reproduction, cause, change, regression evidence, remaining risk,
memory classification, and publication status. Continue through ordinary
commit, delivery-branch push, pull-request, CI, test-integration, and
non-destructive release steps under standing workflow authority. Pause only for
an unapproved governed-instruction change, a destructive production action, or
a material missing product decision. Do not fold unrelated cleanup or
speculative hardening into the bug fix.
