---
name: adopt-workspace-structure
description: Adopt, upgrade, repair, or assess workspace documentation with guided architecture and technology decisions. Use for workspace initialization, version migration, conformance repair, or adoption planning; involve the user in material choices and turn agreed deferred improvements into actionable specs.
metadata:
  skm-version: "0.8.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "671f367253976004e2fe4964b8d55e65aadbd310"
  skm-source-path: "workspace/instructions/skills/adopt-workspace-structure"
  skm-source-integrity: "sha256:0d0eaf27fa2df6a6b61a7bae88ab6a3c2401f0fad7b1421111441644c4cdaa2a"
  workspace-toolkit-version: "0.10.0"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Adopt Workspace Structure

Manage workspace adoption as a project-local, spec-driven migration. Preserve
existing policy and project behavior while bringing documentation, instructions,
specs, and durable memory into the selected `workspace-docs` contract. After
bounded read-only discovery, involve the user in material architecture and
technology decisions before writing project-specific guidance. An observed
stack is evidence of the present, not consent to its future or to a replacement.

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

## Discover and Discuss Project Choices

Inspect only this repository's layout, components, manifests, schemas/migrations,
CI/infrastructure configuration, technical docs and prior user decisions. Do not
read secret values or infer a database from a backend language. Distinguish
observed facts, inferred relationships and unknowns. Keep the target standard's
required workspace structure separate from optional application components.

For adoption, update or repair of project-specific guidance, read
[the project conversation and deferral guide](references/project-conversation.md).
Explain the observed architecture in plain language and ask focused questions
about unresolved goals, constraints and material structure/technology choices.
Use a small relevant batch and wait for actual answers before dependent writes;
continue independent read-only inspection while waiting. Silence is not a choice.
Do not replace this conversation with silent scaffolding or generic approval of
file edits. Reuse answers already provided; a fully specified choice needs no
repeat question or additional routine delivery permission.

Where evidence indicates a problem, explain its concrete effect and compare
proportionate alternatives with benefits, costs, migration risks and constraints.
Keeping a suitable current approach is valid. Let the user choose to address an
improvement now, retain the current approach, or defer with a follow-up spec.
Recommendations are proposals until chosen; adoption authority does not authorize
application refactors or new infrastructure/CI behavior. Resolve policy conflicts
within the named approval scope rather than silently replacing manual policy.

Record confirmed choices, evidence and dispositions in the migration spec/file
map. Add or adapt only the technical guides appropriate to those choices; do not
copy this standards repository's example stack or project structure as target
facts. Missing optional applications need no invented frontend/backend/database.
Assessment reports proposals, questions and possible follow-ups read-only.

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
- each improvement’s required/optional classification, user disposition and
  linked follow-up spec when deferred;
- affected files and product/runtime boundaries;
- validation gates;
- collision, privacy, and rollback risks.
- a `Memory Impact` section initialized to `Status: pending`.

For a fresh adoption where the spec directory does not exist, create only the
minimum directory chain, root specs README from the target template, feature
directory, catalog row, and development spec first. Make no other migration
change until the contract is complete. If existing project policy uses another
spec system, follow it and document the target workspace spec transition.

## Record Agreed Deferred Work

After the user chooses deferral and writing is authorized, create or link one
coherent actionable spec per improvement using the repository's lifecycle and
catalog. Follow the deferral guide for evidence, proposed outcome/options,
concrete actions, dependencies, acceptance, staged validation, risks, version and
memory impact, and the condition for resuming. Keep undecided design choices
explicitly open. Newly deferred work normally enters backlog; already-active
work follows the pinned blocked/resume contract when applicable. Record the
user's reason and cross-link the migration and follow-ups. Do not invent an
owner, deadline, release reservation or implementation permission.

Optional deferred improvements can coexist with completed adoption. Required
manifest/policy/validation failures remain explicit deviations or blockers;
creating a follow-up does not make a failed requirement pass. If the user defers
required work, report partial adoption and retain the incomplete migration state.
Assessment may draft a recommendation in chat but creates no spec, catalog or
memory files without separate write authority.

## Apply the Selected Mode

### Fresh Adoption

1. Preserve or create the root governance files required by the manifest, then
   apply the Claude Instruction Pointer steps below.
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
10. Apply the Claude Instruction Pointer steps below while preserving existing
    manual instructions and resolving occupied paths deliberately.
11. Remove empty legacy paths only after verifying that no current-project
    content was lost.

### Repair

1. Diff the repository structure against the target manifest and audit
   checklist.
2. Repair only confirmed gaps, duplicates, stale markers, or broken links.
3. Preserve compliant content and avoid broad regeneration.
4. Check and repair the Claude pointer only within the approved repair scope.
5. Record why the declared target and actual structure diverged.

### Assessment

Report findings by severity with repository-relative evidence, the detected
mode/version, required migrations, validation gaps, and a proposed explicit
map. Do not create a spec or change files unless the user also requested fixes.

## Claude Instruction Pointer

Apply this compatible skill-level scaffold after root `AGENTS.md` exists; it
adds Claude discovery without changing the selected standard's required-file
contract. Use the [Claude pointer template](templates/CLAUDE.md.template) to
create root `CLAUDE.md`. Copy its content as a regular file at the project root,
not under `workspace/` or the standard directory. Its relative link must resolve
to root `AGENTS.md`; never duplicate policy or copy this repository's manual
instructions into a target project.

- **Fresh adoption:** inspect root `CLAUDE.md` before writing. If absent, create
  it from the template after `AGENTS.md` is created.
- **Update or repair:** if absent or a whitespace-only regular file, create or
  fill it from the template within the approved adoption/repair scope. Do not
  treat a file containing comments, imports, or instructions as empty.
- **Existing content:** preserve substantive `CLAUDE.md` bytes and manual rules.
  If it already points to root `AGENTS.md`, verify that target. If it does not,
  report the missing pointer as a deviation and propose adding it; do not
  replace or prepend policy silently or declare the pointer gate satisfied.
- **Conflicting paths:** inspect symlinks, directories, dangling links, and
  conflicting destinations before any write. Do not follow an external target,
  replace a symlink, or overwrite a directory. Preserve it and report the
  collision for an explicit project-local resolution.
- **Assessment:** report a missing, empty, invalid, or unresolved pointer
  without creating files or changing existing instructions.

Verify the resulting regular file or deliberately preserved in-repository
pointer, its root-relative AGENTS.md target, and preserved manual content.
Record the pointer result and any unresolved deviation in the migration spec
and handoff. Missing or invalid template resources block creation; do not invent
an empty file or infer success from the source repository's own CLAUDE.md.

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

1. Verify material choices were answered before dependent writes, every agreed
   deferral has its actionable spec/catalog link, and required gaps are not
   presented as optional improvement. Compare the final structure with the
   target manifest and audit checklist;
   separately verify the Claude pointer and preserved-content deviations.
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
- Claude pointer validation and preservation of existing Claude instructions;
- validation commands and results;
- memory-impact classification and rationale;
- confirmed architecture/technology decisions and their rationale;
- deferred improvement spec links, resume conditions and unresolved required gaps;
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
For v7 development and review fixes, map changed behavior and direct/transitive
consumers, including interfaces, errors, security, timing, side effects,
configuration, dependencies, and generated outputs. Run the smallest meaningful
changed-component tests/checks first; only after they pass, run affected consumer
checks in dependency order through the transitive chain. Failure blocks dependent
stages; missing coverage or tools is a gap, never a pass. Deduplicate overlapping
checks, assess old/new relationships for deletions and renames, and group cycles.
Avoid unrelated aggregate runs; unknown impact requires justified safe fallback.
Keep required contract/integration/end-to-end coverage and native CI protections.
Reuse only proven-fresh evidence after further edits; a flat selection is not
execution order. Read-only skills assess evidence without mutating; planning
skills specify stages without implementing. Reconcile
knowable spec, catalog, and memory records before required review. Finish review,
artifacts, documentation, records, and fixes before freezing the candidate and
running full required checks/tests. Later tracked event/result records renew
affected review and verification; they do not automatically preserve evidence. Reuse only proven-fresh evidence and verify actual
combined integration/main revisions. Each acceptance criterion needs supporting
evidence; subjective product decisions go to the user. Read-only skills remain
read-only and planning skills do not implement changes.
