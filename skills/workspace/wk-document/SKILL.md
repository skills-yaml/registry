---
name: wk-document
description: Run the wk.document lifecycle facade to create or maintain human-facing project documentation within repository ownership boundaries. Invoke explicitly when documentation must be reconciled with current behavior and validated.
metadata:
  skm-version: "0.1.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "6dbdf01341a8ab5d572179462f1b460ff6259c51"
  skm-source-path: "workspace/instructions/skills/wk-document"
  skm-source-integrity: "sha256:88fe49cfb973aa25182cf64ffd6ec1411ac86cab92fcc8499e224bfb12ad252d"
  workspace-toolkit-version: "0.3.0"
  workspace-docs-compatibility: "5.x"
  minimum-skm-version: "0.4.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/maintain-project-docs@0.1.0"
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
