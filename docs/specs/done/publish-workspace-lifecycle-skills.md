# Done Spec: Publish Workspace Lifecycle Skills

## Status

State: `done`

Rationale: Registry PR #1 published the Workspace packages through `main` at
`3b6a8cc6a62ce881e10731828cd73bafc8383605`; main CI run `34427475083` passed.
The packages pin Workspace production revision
`fb4aa64a6121f1f8a57d4848b52fa0ec7cefd452`. The released SKM 0.4.0 binary
cloned the published registry, installed `wk-deliver` and its eight exact
dependencies, passed `skm check`, and converged with all nine links unchanged
on a second apply.

## Summary

Publish the Workspace project's independently versioned skills under the
`workspace` registry namespace. Preserve immutable exact versions, expose
`latest` and `default` aliases, carry source provenance and exact dependency
metadata, and add deterministic registry checks that enforce the package
contract consumed by SKM 0.4.0 and later.

## Scope

- Add the generated Workspace skill packages at `skills/workspace/<skill-id>`.
- Publish both focused capabilities and explicit `wk-*` lifecycle facades.
- Preserve every exact `vMAJOR.MINOR.PATCH` directory as an immutable package.
- Validate skill identity, structure, aliases, metadata, dependencies,
  provenance, integrity, path containment, and release immutability.
- Add Taskfile entrypoints and offline regression tests for registry checks.
- Update the registry catalog, structure, versioning, project inventory, and
  durable memory for the new namespace and release contract.
- Prove installation and convergence using the released SKM 0.4.0 consumer.

## Out of Scope

- Changing the Workspace package contents after they are generated.
- Adding registry-hosted agent profiles or Workspace toolkit manifests; those
  remain versioned in the Workspace source repository.
- Adding non-exact dependency constraints or dependencies across registries.
- Retrofitting provenance metadata into unrelated existing registry packages.
- Redesigning the full registry publication or release service.

## Acceptance Criteria

1. `skills/workspace/` contains the complete package set declared by Workspace
   toolkit 0.3.0, with exact version directories and root/current copies.
2. Every package has contained `latest` and `default` aliases targeting a real
   exact version directory, and the root/current content matches `latest`.
3. Every Workspace `SKILL.md` has Agent Skills-compatible string metadata for
   SKM schema version, canonical source repository, full source revision,
   canonical source path and integrity, toolkit and Workspace Docs versions,
   minimum SKM version, adapter compatibility, and exact dependencies when
   present.
4. Dependency references use `workspace/<skill-id>@MAJOR.MINOR.PATCH`, resolve
   to published exact versions, contain no cycles, and agree between root and
   versioned package copies.
5. Registry validation rejects malformed identities, unsafe paths and
   symlinks, invalid aliases, inconsistent copies, bad provenance, missing or
   cyclic dependencies, and modifications to an exact version already present
   in the comparison Git revision.
6. Representative success and failure fixtures exercise all new validator
   boundaries without network access.
7. Taskfile `check` and `test` entrypoints run the registry validation and test
   suite deterministically.
8. Pull requests and `main` run the Taskfile gates in read-only registry CI.
9. README and registry contracts explain namespace lookup, independent SemVer,
   dependency metadata, aliases, publication, and direct invocation of the
   hyphenated `wk-*` package names.
10. A released SKM 0.4.0 binary installs a representative lifecycle facade and
   its exact transitive dependencies from this registry, `skm check` succeeds,
   and a second apply reports the same dependency links as already installed.

## Affected Areas

- `skills/workspace/`
- `scripts/validate_registry.py`
- `scripts/test_validate_registry.py`
- `Taskfile.yml`
- `.github/workflows/ci.yml`
- `README.md`
- `SKILL_STRUCTURE.md`
- `VERSIONING.md`
- `docs/projects/registry/inventory.md`
- `docs/specs/README.md`
- `agents/memory/`

## Implementation Plan

1. Add the active spec and task-runner contract.
2. Implement the registry validator, regression fixtures, and CI enforcement.
3. Generate packages from a clean, revision-verified Workspace source tree.
4. Update registry documentation and durable memory.
5. Run local gates, perform correctness and security review, and fix findings.
6. Integrate through the repository delivery workflow.
7. After Workspace production release, regenerate or verify provenance against
   the released source revision and complete end-to-end SKM validation.
8. Reconcile this spec to `done` only after all acceptance criteria pass.

## Validation Gates

- `task check`
- `task test`
- `git diff --check`
- Workspace package generator with `--verify-revision`
- released SKM 0.4.0 install/check/convergence test
- Git comparison against the production base for exact-version immutability

## Risks and Mitigations

- **Mutable releases:** compare exact version trees to the production base and
  reject any deletion or content/type change.
- **Path or symlink escape:** reject symlinks below package payloads and require
  aliases to target contained, real exact version directories.
- **Dependency confusion:** accept only exact same-registry coordinates and
  validate the complete dependency graph.
- **Provenance drift:** generate from a clean Workspace revision, embed canonical
  source paths and hashes, and require root/version metadata agreement.
- **Consumer incompatibility:** pin the minimum SKM and adapter contract and
  exercise the released binary before completion.

## Memory Impact

Status: `updated`

Rationale: The durable namespace and publication contract are recorded in
`agents/memory/decisions.md`. The released package set, source and registry
revisions, CI evidence, and SKM compatibility are recorded in
`agents/memory/facts.md`; corresponding entries are in
`agents/memory/changelog.md`.
