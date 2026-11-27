---
name: wk-spec
description: Explicitly invoke wk.spec to turn an accepted request into a development specification through write-spec.
metadata:
  skm-version: "0.5.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "59e8ad3a02a57ad1b5b659fd9deb752e627ee893"
  skm-source-path: "workspace/instructions/skills/wk-spec"
  skm-source-integrity: "sha256:f254ff7ef23fc762792816d4331c994b2c06cfef7a15e781dbdcf77e8bd0327b"
  workspace-toolkit-version: "0.19.0"
  workspace-docs-compatibility: "11.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.8.1"
---

# wk.spec

Use this facade only when explicitly requested. Require `write-spec`; if the
dependency is unavailable or incompatible, report an actionable installation
or compatibility error before proceeding.

Route the accepted request through that focused workflow. It owns discovery,
questions, impact assessment, spec contents, decomposition, readiness,
catalog/version/memory records, review and validation under the consuming
project's actual pinned SDLC. Keep those requirements in the focused workflow
and its authoritative references.

Return its spec path, ready/blocked work, unresolved decisions, validation and
next allowed transition. This facade delivers planning artifacts; it does not
start feature implementation or grant approval to change governed instructions.

## Unfinished Work Notice

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
