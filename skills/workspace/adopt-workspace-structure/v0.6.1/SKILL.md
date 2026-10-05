---
name: adopt-workspace-structure
description: Adopt, upgrade, repair, or assess the workspace-docs repository structure and its agent governance. Use when an agent must initialize workspace documentation in a project, migrate workspace-docs 1.x or 2.0 layouts to a newer version, update an existing pinned version, repair a partial or mixed adoption, check conformance and implement requested fixes, or complete and validate an in-progress workspace migration.
metadata:
  skm-version: "0.6.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "f867573bc91b5560d12cebd304ba3dd98aed7435"
  skm-source-path: "workspace/instructions/skills/adopt-workspace-structure"
  skm-source-integrity: "sha256:1cc215d7c21f73bba4def912d50585b2d08d90c78b375033230eff220d799a50"
  workspace-toolkit-version: "0.7.1"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Adopt Workspace Structure

Manage workspace adoption as a project-local, spec-driven migration. Preserve
existing policy and project behavior while bringing documentation, instructions,
specs, and durable memory into the selected `workspace-docs` contract.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. Historical packages apply
only when pinned; report unresolved conflicts between current instruction files.

## Establish Authority and Scope

1. Determine whether the user requested assessment only or authorized changes.
   Keep assessment requests read-only; do not infer permission to migrate.
2. Treat a direct human request to adopt, upgrade, repair, or migrate the
   workspace as prospective instruction-change approval only for the governed
   instructions necessary to that named target. A general implementation or
   delivery request is not approval. Do not edit governed instructions first
   and request approval afterward.
3. Resolve the current repository root and operate only inside it. Do not
   inspect parent directories, sibling repositories, or machine-wide state.
4. Read the repository's existing `AGENTS.md`, `DESIGN.md`, `README.md`, task
   and SDLC guidance, `workspace/specs/README.md`, relevant specs, and durable
   memory before editing. Record required files that do not exist as adoption
   gaps.
5. Inspect the branch, status, and current tree. Preserve unrelated and
   pre-existing user changes.
6. Identify the current pinned `workspace-docs@X.Y.Z` version, if any, and the
   target version requested by the user.

If two or more agents may mutate the repository concurrently, invoke
`coordinate-multi-agent-development` before delegated edits. Give each
mutating agent a dedicated detached worktree and repository WIP record; keep
the primary checkout coordination-only. Ordinary task or delivery branches follow task authority under Workspace Docs 7;
older pins retain their direct branch-request requirement. Always honor protections.

If no target is specified, use the concrete version referenced by the selected
standard package's `default` pointer. Never silently select a downgrade.

## Resolve the Trusted Standard

Use a standard package from this order:

1. The current repository's `workspace/instructions/standards/workspace-docs/`.
2. A source explicitly provided by the user.
3. The [bundled workspace-docs standard](references/workspace-docs/README.md)
   that ships with this skill. It includes the canonical
   [Agent Migration Guide](references/workspace-docs/AGENT_MIGRATION.md),
   versioning rules, every versioned manifest, template, audit checklist, and
   migration note from the source standard tree. Use it without network access
   or another checkout when neither of the first two sources is available.
4. The documented canonical `skills-yaml/workspace` repository when network
   access and the requested operation authorize retrieval.

The bundled `default` and `latest` are plain-text pointer files because portable
skill packages cannot contain source symlinks. Read their version-directory
names; do not treat them as version directories. When installing the complete
bundled standard in the current project, copy its regular files and version
directories to `workspace/instructions/standards/workspace-docs/`, then create
contained relative `default` and `latest` symlinks to the named directories.
Check occupied destinations before copying, and never overwrite a different
standard tree silently. Do not copy the plain-text pointers as alias files.

Pin a concrete version before copying or editing. Never discover a standard by
searching unrelated local projects. If the bundled copy is missing or invalid
and no other trusted package is available, stop and report the required input.

Read these resources completely from the selected package:

- `AGENT_MIGRATION.md`
- `<target-version>/manifest.yaml`
- `<target-version>/sdlc.md`
- `<target-version>/process.md`
- `<target-version>/agents-template.md`
- `<target-version>/audit-checklist.md`
- `<target-version>/specs-readme-template.md` when the target contract provides
  it
- `<target-version>/migration.md` for an update or repair

Read intermediate migration notes when crossing more than one released
version. Treat the target manifest as the structural source of truth.

## Classify the Work

Choose one mode and record it:

- **Fresh adoption**: no workspace documentation structure exists.
- **Version update**: an older version is pinned or an older canonical layout
  exists.
- **Repair**: the target version is declared but the structure is incomplete,
  duplicated, or inconsistent.
- **Assessment**: inspect conformance and report findings without changing
  files.

Treat mixed layouts as an update. Do not scaffold a second copy alongside
existing content.

## Discover and Confirm Project Choices

Before a mutating adoption or an update to project-specific documentation,
inspect only the current repository for its application layout, components,
build and dependency manifests, database schemas or migration configuration,
infrastructure and CI files, existing technical documentation, and decisions
already stated by the user. Do not read secret values. Separate observed facts
from inferences and unknowns; a backend language does not establish a database
choice, and this standards repository's application examples are not a target
project's architecture.

Propose the project-specific structure and the exact technical guides to add,
adapt, retain, or omit, with repository-relative evidence for each choice. Keep
the target standard's required `workspace/` structure distinct from optional
application directories. When repository evidence supports a proposal, ask the
user to approve or correct it before changing project-specific files. When
there is no evidence for an application layout or stack, ask the user which
structure and technologies they want, including whether the project has no
backend, database, frontend, or infrastructure component. For partial evidence,
ask only about material gaps. A clear choice already supplied in the user's
request is the answer; do not request duplicate approval.

Record the confirmed choices and evidence in the migration spec and explicit
file map. Do not copy this repository's project-specific `project_structure.md`
or conditional backend, frontend, CI, infrastructure, or database guidance as
target-project facts. Adapt or create such guidance only when the confirmed
project plan calls for it, preserving existing authoritative content. If the
user chooses a layout that conflicts with the selected standard, explain the
conflict and resolve the target or documented deviation before editing. In
assessment mode, report the proposal and open choices without changing files.

## Create the Migration Contract

Before non-trivial changes, create or move a migration spec into
`workspace/specs/development/<primary-feature>/` according to local policy.
Use `workspace-governance` unless the repository defines a more accurate
primary feature. Add or update the spec's row in `workspace/specs/README.md` in
the same change, including its state and the reason work is active. Include:

- current and target versions;
- migration mode and scope;
- acceptance criteria;
- an explicit source, destination, and merge decision for every moved area;
- the repository evidence and confirmed project structure, technology choices,
  and conditional guides to add or omit;
- affected files and product/runtime boundaries;
- validation gates;
- collision, privacy, and rollback risks.
- a `Memory Impact` section initialized to `Status: pending`.

For a fresh adoption where the spec directory does not exist, create only the
minimum directory chain, root specs README from the target template, feature
directory, catalog row, and development spec first. Make no other migration
change until the contract is complete. If existing project policy uses another
spec system, follow it and document the target workspace spec transition.

## Apply the Selected Mode

### Fresh Adoption

1. Preserve or create the root governance files required by the manifest.
2. Create the required `workspace/` directories without claiming optional
   project content exists.
3. Add the pinned standard package and only the project-specific technical
   instructions supported by the confirmed structure and technology choices.
4. Insert the generated context from `agents-template.md` between one balanced
   pair of `AGENT-CONTEXT` markers.
5. Keep all manual `AGENTS.md` rules outside the generated block unchanged.
6. Initialize durable memory with stable current-project information only.
7. Add real Taskfile validation and test entrypoints; never add no-op gates.
8. Add the target version's memory-impact completion gate. Record the adoption
   decision in the appropriate category file and `changelog.md`.
9. Add the target version's spec-catalog gate and categorize any current specs
   by their primary feature without changing their lifecycle state.

### Version Update

1. Apply each required version boundary in order.
2. Create destinations before moving content.
3. Execute the spec's explicit migration map one area at a time.
4. Stop on an occupied destination or ambiguous duplicate. Inspect and merge
   deliberately; never overwrite or suppress the failure.
5. Replace only the generated `AGENT-CONTEXT` block with the target template.
6. Update repository-relative links, Taskfile paths, tooling references, and CI
   references affected by file moves without changing unrelated behavior.
7. Reconcile durable memory by preserving stable facts, superseding obsolete
   entries, and removing unsafe or unrelated local context.
8. Add or update the deterministic memory-impact gate required by the target
   standard version.
9. Categorize current specs, create or update the root specs catalog, and add
   the deterministic spec-catalog gate required by the target version.
10. Remove empty legacy paths only after verifying that no current-project
   content was lost.

### Repair

1. Diff the repository structure against the target manifest and audit
   checklist.
2. Repair only confirmed gaps, duplicates, stale markers, or broken links.
3. Preserve compliant content and avoid broad regeneration.
4. Record why the declared target and actual structure diverged.

### Assessment

Report findings by severity with repository-relative evidence, the detected
mode/version, required migrations, validation gaps, and a proposed explicit
map. Do not create a spec or change files unless the user also requested fixes.

## Enforce Migration Boundaries

- Keep all project-specific information limited to the current repository.
- Use repository-relative paths in files, commits, pull requests, issues, and
  handoffs.
- Never migrate secrets, credentials, environment values, caches, dependency
  trees, build artifacts, machine identities, absolute local paths, or
  cross-project inventories.
- Do not change application behavior, authentication, authorization, data
  flow, infrastructure, or CI/CD behavior unless explicitly in scope.
- Do not delete ambiguous content. Stop and request direction when ownership or
  merge precedence cannot be established safely.
- A requested migration implementation has standing workflow authority for
  commits, pull-request updates, bounded CI work, and non-destructive delivery.
  Ordinary branch creation and pushing follow the pinned SDLC authority. Do not request repeated approval for the remaining steps or
  bypass repository protection. Pause for prospective human approval when a
  governed instruction is outside the directly approved migration scope, and
  for scoped approval before a destructive production action.

## Validate and Complete

1. Compare the final structure with the target manifest and audit checklist.
2. Confirm instructions, specs, docs, and memory have one active canonical location.
3. Confirm one balanced generated context block pins the concrete target and
   manual policy is preserved unless its reconciliation was explicitly approved.
4. Search current documents for obsolete markers, paths, machine-local content,
   and unrelated-project context; preserve intentionally historical packages.
5. Validate current-document relative links.
6. Run affected Taskfile modules during coherent edits and review fixes.
7. Self-review the full diff for unintended changes and scope growth.
8. Confirm in-scope memory classifications are valid. The native gate rejects
   missing/incomplete records and permits pending only where the pinned contract
   allows a genuinely unresolved outcome.
9. Confirm every non-legacy spec has one feature path and a matching catalog row.
10. Classify and record the migration's knowable memory impact, adopted version,
    durable project decisions, and changelog before review and final verification.
11. Reconcile knowable acceptance evidence, memory, and deviations in the active
    spec and catalog. Do not invent integration or publication evidence.
12. Obtain independent exact-candidate review for governed instruction changes
    and other changes required by the pinned risk rules. Resolve every finding,
    rerun affected modules, and renew review for relevant edits. Once records,
    artifacts, documentation, and fixes stabilize, freeze the candidate and run
    `task check`, `task test`, and applicable project gates. Reuse only proven-
    fresh native evidence and preserve Taskfile/protection boundaries.
13. Local migration remains in development. Move to test only after confirmed
    shared-test integration, conventionally `develop`, with catalog evidence.
14. Move to done only on the pinned completion event: verified main merge and
    reconciled acceptance/records in v7. A documented direct-to-main route keeps
    every gate; older pins retain their completion contract. Track publication
    separately and never infer events from a branch name.
15. Report final results at handoff. Later tracked result/integration records
    and changed combined revisions require affected review and verification
    reconciliation; do not assume these writes preserve the frozen candidate.

Do not declare completion while required checks fail, collisions remain, or the
spec state disagrees with actual delivery evidence.

## Hand Off

Lead with the outcome and include:

- migration mode;
- previous and target versions;
- significant repository-relative moves or merges;
- confirmation that manual `AGENTS.md` policy was preserved;
- validation commands and results;
- memory-impact classification and rationale;
- deviations, blockers, or follow-up work;
- publication and lifecycle status.

Never include machine-local paths, identities, sibling-project details,
credentials, or environment-specific values in the handoff.

## Pinned SDLC Contract

Read the project's pinned SDLC before planning or delivery. For Workspace Docs
7, done means verified merge into main with reconciled acceptance, documentation,
catalog, version records, and memory; deployment/publication is separate.
Blocked records previous stage, kind, reason, and resume condition; resume there
and renew stale evidence. Preserve done history with linked follow-up specs.
Shared test integration is the default; only an explicitly documented direct
route may omit it, preserving all gates. Older pins keep their prior completion
and branch-authority contracts.

For v7, the task request authorizes ordinary task branches and safe delivery.
Security, data integrity, public interfaces, governed instructions, and release
controls always require independent exact-candidate review; other non-trivial
changes require it except small low-risk changes with focused tests.
Resolve every finding by implementation or reviewer-agreed documented rejection.
Run affected modular gates during implementation and review fixes. Reconcile
knowable spec, catalog, and memory records before required review. Finish review,
artifacts, documentation, records, and fixes before freezing the candidate and
running full required checks/tests. Later tracked event/result records renew
affected review and verification; they do not automatically preserve evidence. Reuse only proven-fresh evidence and verify actual
combined integration/main revisions. Each acceptance criterion needs supporting
evidence; subjective product decisions go to the user. Read-only skills remain
read-only and planning skills do not implement changes.
