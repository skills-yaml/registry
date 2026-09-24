---
name: maintain-project-docs
description: Create, update, reconcile, or review human-facing project documentation within repository-declared documentation roots. Use when project reference, architecture, operational, onboarding, or work documentation must reflect current repository behavior without changing governed agent instructions.
metadata:
  skm-version: "0.2.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "bd958c01249e1cb1e1fbbcf91ba70e83abec8d5f"
  skm-source-path: "workspace/instructions/skills/maintain-project-docs"
  skm-source-integrity: "sha256:a182b2496f62e0babc5d9f46b5ab8618f63c41dc542da507878aa8160a0ce7b3"
  workspace-toolkit-version: "0.4.0"
  workspace-docs-compatibility: "6.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Maintain Project Documentation

Keep project documentation accurate, connected, and within its declared
ownership boundary.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. Governed instruction changes
require prospective human instruction-change approval for the named scope.

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

If two or more agents may mutate the repository concurrently, invoke
`coordinate-multi-agent-development` before delegated edits. Give each
mutating agent a dedicated detached worktree and repository WIP record; keep
the primary checkout coordination-only. A task or delivery branch may be
created or selected only when the user directly requested branch use for the
named task.

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

After the user requests the documentation change, standing workflow authority
covers its ordinary edits, validation, commits, pull-request updates, CI work,
and non-destructive release steps. Create or push a task or delivery branch
only after the direct branch request required above. Pause for an unapproved
governed instruction change, a destructive production action, or a material
missing product decision.
