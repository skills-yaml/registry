---
name: maintain-project-docs
description: Create, update, reconcile, or review human-facing project documentation within repository-declared documentation roots. Use when project reference, architecture, operational, onboarding, or work documentation must reflect current repository behavior without changing governed agent instructions.
metadata:
  skm-version: "0.1.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "6dbdf01341a8ab5d572179462f1b460ff6259c51"
  skm-source-path: "workspace/instructions/skills/maintain-project-docs"
  skm-source-integrity: "sha256:32ae83701cd526406c467daac9171834cf361e67e1945181324c4650246bae20"
  workspace-toolkit-version: "0.3.0"
  workspace-docs-compatibility: "5.x"
  minimum-skm-version: "0.4.0"
  skm-adapter-compatibility: "2.x"
---

# Maintain Project Documentation

Keep project documentation accurate, connected, and within its declared
ownership boundary.

## Establish Authority and Sources

1. Read repository policy, documentation ownership rules, nearby documents,
   relevant implementation, and active specifications.
2. Determine whether the request is documentation-only or follows an
   implementation change. Treat current behavior and authoritative instructions
   as evidence; report conflicts instead of copying stale text.
3. Write only within human-facing documentation roots declared by the
   repository. Do not edit root agent policy, design tokens, or files under
   `workspace/instructions/` unless the human request explicitly names that
   governed instruction scope.

## Maintain the Documentation

- Use the repository's established structure, terminology, and link style.
- Prefer links to authoritative policies over duplicated procedural text.
- Describe only the current project and use repository-relative paths in
  committed content.
- Keep examples safe, deterministic, and free of secrets or machine-local
  information.
- Reconcile affected indexes, navigation, diagrams, and nearby references when
  the requested change makes them stale.
- Preserve manual content and unrelated work.

## Validate and Hand Off

Run the repository's documented documentation and aggregate validation gates.
Review the final diff for factual accuracy, broken links, accidental policy
changes, and local-information leakage. Classify memory impact under local
policy and report the documents changed, validation performed, and any known
gap or intentionally deferred update.
