---
name: wk-document
description: Run the wk.document lifecycle facade to create or maintain human-facing project documentation within repository ownership boundaries. Invoke explicitly when documentation must be reconciled with current behavior and validated.
metadata:
  skm-version: "0.4.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "59e8ad3a02a57ad1b5b659fd9deb752e627ee893"
  skm-source-path: "workspace/instructions/skills/wk-document"
  skm-source-integrity: "sha256:6875dc3eeccc950667b735e863ac9865848baffcc8092a056faa9e07c7511d82"
  workspace-toolkit-version: "0.19.0"
  workspace-docs-compatibility: "11.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/maintain-project-docs@0.4.1"
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
resolve required review before freezing the candidate and running the pinned final
gates. Reconcile the pinned lifecycle without claiming completion or publication
from documentation changes alone.

## Pinned SDLC Contract

Read the repository's pinned SDLC; this skill does not override its authority
or this skill's applicable mode and authority boundaries. Deliver the requested
scope using existing patterns. Report optional improvements separately and leave them
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

- v9 and later: changed behavior and all affected direct/transitive consumers locally;
  every required affected CI job on the stable candidate. Docs/spec, backend
  and frontend changes skip unrelated jobs. Preserve required status names,
  validated selection and dependency stages. No blanket full-repository run.
- v8: the same affected local boundary, then complete required gates in CI.
  Neither v8 nor any later pin requires a duplicate full local run before CI. Missing CI
  cannot establish final acceptance; unknown impact needs investigation and
  justified CI fallback.
- v7: affected modules during iteration, then full required final-candidate
  checks/tests after review and fixes. Earlier pins retain their own contract.

During development and review fixes, pass changed-component checks before
consumer checks in dependency order. Include interfaces, errors, security,
timing, side effects, configuration, dependencies and generated outputs in
impact analysis. Failures block dependent stages; deduplicate checks, assess
old/new relationships for moves/deletions and group cycles. Reuse only proven-
fresh evidence. Apply these checks only within the authorized mode and scope.
Work on one active task per agent. Split oversized specs into bounded ordered
steps with prerequisites, acceptance mapping and focused validation; use linked
child specs for independently deliverable work and preserve overall acceptance.

For v11 and later, follow the pinned SDLC's Unfinished Work Notice: if the task
ends before its requested outcome is fully delivered, start the final hand-off
with `**Not finished:**` and one plain sentence naming what is not done. Then
state what was done so far, why it stopped in everyday words, numbered possible
fixes saying who must act with one recommended, and where the work is
preserved. The notice is the only text allowed before a fixed report template,
which still follows in full. A report that delivers its findings is finished
even when they show failures. Explain any error or internal term, never
present partial work as complete, and relay unfinished subagent or peer
hand-offs the same way.
