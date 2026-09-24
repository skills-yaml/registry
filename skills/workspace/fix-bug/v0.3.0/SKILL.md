---
name: fix-bug
description: Reproduce, isolate, and fix a reported software defect with regression coverage. Use when observed behavior differs from a requirement or established contract and the user authorizes a focused implementation change.
metadata:
  skm-version: "0.3.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "bd958c01249e1cb1e1fbbcf91ba70e83abec8d5f"
  skm-source-path: "workspace/instructions/skills/fix-bug"
  skm-source-integrity: "sha256:0843a29b1a74fa48f8c472717c94a8268b912a4307ad56a5007a1a23a59197bd"
  workspace-toolkit-version: "0.4.0"
  workspace-docs-compatibility: "6.x"
  minimum-skm-version: "0.7.0"
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

If two or more agents may mutate the repository concurrently, invoke
`coordinate-multi-agent-development` before delegated edits. Give each
mutating agent a dedicated detached worktree and repository WIP record; keep
the primary checkout coordination-only. A task or delivery branch may be
created or selected only when the user directly requested branch use for the
named task.

Treat governed instructions as read-only unless a direct human request
prospectively grants instruction-change approval for the named outcome or
scope. A general bug-fix request and standing workflow authority do not include
that permission. Do not edit governed instructions and seek approval
retroactively.

## Fix and Prove

1. Add a regression test that fails for the confirmed defect where feasible.
2. Implement the smallest coherent correction using established patterns.
3. Test boundary inputs, error paths, compatibility, and adjacent behavior.
4. Run the narrowest repository-owned focused checks until the reproduction and
   representative failure paths pass. Regenerate affected artifacts first.
5. Self-review the complete diff against the reproduction, expected contract,
   affected consumers, and relevant security or persistence boundaries.
6. Stabilize the candidate and run all required final repository gates. Reuse a
   prior result only through the repository's deterministic freshness contract.
7. Reconcile the active spec, root catalog, and memory impact when local policy
   requires them. Keep the spec in development until confirmed test-target
   integration, then move it to test; move it to done only after confirmed
   production release.

For infrastructure defects, change OpenTofu configuration and run non-mutating
validation locally. Apply, destroy, import, and state correction must run only
through the repository's CI/CD Taskfile workflow. Any proposed local, direct,
provider-CLI, or alternative-engine mutation path is a blocker, not a fallback.

Report the reproduction, cause, change, regression evidence, remaining risk,
memory classification, and publication status. Continue through ordinary
commit, pull-request, CI, test-integration, and non-destructive release steps
under standing workflow authority. Create or push a task or delivery branch
only after the direct branch request required above. Pause only for an
unapproved governed-instruction change, a destructive production action, or a
material missing product decision. Do not fold unrelated cleanup or speculative
hardening into the bug fix.
