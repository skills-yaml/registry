---
name: wk-spec
description: Explicitly invoke wk.spec to turn an accepted request into a development specification through write-spec.
metadata:
  skm-version: "0.4.7"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "6a99cb76b2f06ee9e49ba8a21f29356f41d9b2d0"
  skm-source-path: "workspace/instructions/skills/wk-spec"
  skm-source-integrity: "sha256:075a453b8d92bdbe8a08b692f6bbcca44c031a207ca2ff171e1221533f3305f8"
  workspace-toolkit-version: "0.14.1"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.6.5"
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
