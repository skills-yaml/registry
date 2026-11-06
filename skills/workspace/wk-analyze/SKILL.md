---
name: wk-analyze
description: Run the wk.analyze lifecycle facade to produce a read-only, evidence-backed repository assessment. Invoke explicitly when the user wants repository structure, stack, SDLC, policy, documentation, active-work, risk, and gap analysis.
metadata:
  skm-version: "0.4.7"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "6a99cb76b2f06ee9e49ba8a21f29356f41d9b2d0"
  skm-source-path: "workspace/instructions/skills/wk-analyze"
  skm-source-integrity: "sha256:9dfb6a9092cbd867a994e8b7eeb4a986ac4b1071bce0e10dc90f8a8a4d3be986"
  workspace-toolkit-version: "0.14.1"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/analyze-repository@0.4.7"
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

## Pinned SDLC Contract

Read the repository's pinned SDLC; this skill does not override its authority
or this skill's read-only/planning boundary. Deliver the requested scope using
existing patterns. Report optional improvements separately and leave them
unimplemented. Before substantial scope expansion, identify the concrete
blocker, propose the smallest solution and obtain approval. Standing workflow
authority never grants unrelated work or governed instruction changes.

For v7 and later, ordinary task branches and safe delivery follow task authority.
Done means verified main merge with acceptance, documentation, catalog, versions
and memory reconciled; publication is separate. Preserve done history with
linked follow-ups. Blocked work records previous stage, kind, reason and resume
condition; resume that stage with renewed evidence. Shared test integration is
the default; a documented direct route preserves the same gates.

Security, data integrity, public interfaces, governed instructions and release
controls require independent exact-candidate review. Other non-trivial changes
require it except small low-risk changes with focused tests. Resolve findings
by a fix or reviewer-agreed documented rejection; optional suggestions remain
outside scope. Finish relevant review, fixes, artifacts and knowable records
before final verification. Later edits renew affected evidence. Verify actual
combined integration/main revisions, record acceptance evidence and preserve
host protections; missing coverage/tools are gaps, never a pass.

Use the verification contract for the actual pin:

- v9: changed behavior and all affected direct/transitive consumers locally;
  every required affected CI job on the stable candidate. Docs/spec, backend
  and frontend changes skip unrelated jobs. Preserve required status names,
  validated selection and dependency stages. No blanket full-repository run.
- v8: the same affected local boundary, then complete required gates in CI.
  Neither v8 nor v9 requires a duplicate full local run before CI. Missing CI
  cannot establish final acceptance; unknown impact needs investigation and
  justified CI fallback.
- v7: affected modules during iteration, then full required final-candidate
  checks/tests after review and fixes. Earlier pins retain their own contract.

During development and review fixes, pass changed-component checks before
consumer checks in dependency order. Include interfaces, errors, security,
timing, side effects, configuration, dependencies and generated outputs in
impact analysis. Failures block dependent stages; deduplicate checks, assess
old/new relationships for moves/deletions and group cycles. Reuse only proven-
fresh evidence. Read-only work assesses this evidence; planning specifies it.
Work on one active task per agent. Split oversized specs into bounded ordered
steps with prerequisites, acceptance mapping and focused validation; use linked
child specs for independently deliverable work and preserve overall acceptance.
