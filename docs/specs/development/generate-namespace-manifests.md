# Spec: Generate Namespace Manifests

Status: Development

Purpose: Stop authors from copying package versions into namespace manifests by
hand, and publish the `skills-yaml/authoring-toolkit` bundle.

## 1. Problem Statement

A schema-2 namespace manifest lists every package with its current version, and
each bundle then names the packages it contains:

```yaml
packages:
  skill-creator: "0.1.0"
  skill-reviewer: "0.1.0"
bundles:
  authoring-toolkit:
    packages: [skill-creator, skill-reviewer]
```

The version numbers repeat information that is already in each package's
`SKILL.md` and `latest` alias. The validator requires the `packages` section to
match the published versions exactly, so the repetition is safe, but it means an
author has to edit two places whenever a package is released.

The Workspace manifest avoids this because the Workspace packager generates it.
Manifests written by hand, such as the one for `skills-yaml`, had no such tool.

Changing the format to drop the `packages` section was considered and rejected.
SKM reads bundle versions from that section, and every SKM that already reads
bundles would stop seeing a manifest without it.

## 2. Goals and Non-Goals

### Goals

- Let authors write only the `bundles` section of a hand-maintained manifest.
- Generate the rest of the file from the package folders.
- Keep the published format unchanged, so current SKM releases read it.
- Publish `skills-yaml/authoring-toolkit`.

### Non-Goals

- Changing the manifest format.
- Generating or modifying the Workspace manifest, which the Workspace packager
  owns together with its provenance fields.
- Creating manifests for namespaces that do not have one. A manifest stays
  optional, and the author creates it by writing its `bundles` section.

## 3. Design

`scripts/generate_manifests.py`, run as `task manifest`:

1. For every namespace except `workspace` that has a `manifest.yaml`, read the
   author's `bundles` section.
2. Build the `packages` section from each package's `latest` alias.
3. Write the file in a fixed order, with a comment explaining which part is
   generated.
4. Refuse to write, and leave the file unchanged, when a bundle names a package
   that is not published, when a field is unknown, or when the YAML is invalid.

`--check` reports stale manifests without writing them. The existing validator
already fails `task check` when the `packages` section is out of date, so the
generator does not add a gate of its own.

## 4. Verification and Acceptance Criteria

- [x] Running `task manifest` on a file containing only `bundles` produces a
      complete manifest that passes the validator.
- [x] The output is sorted and a second run changes nothing.
- [x] A new release updates the `packages` section on the next run.
- [x] Unknown bundle members and unknown fields are rejected without writing.
- [x] The Workspace manifest and namespaces without a manifest are left alone.
- [x] `skills/skills-yaml/manifest.yaml` publishes `authoring-toolkit`.
- [x] SKM 0.7.0 lists the bundle in `skm search`, resolves it in
      `skm add --kind bundle --dry-run`, writes both members pinned to 0.1.0,
      passes `skm check`, and changes nothing on a second apply. Verified
      against a local copy of this branch on 2026-09-24.
- [x] `task check` and `task test` pass.

## 5. Integration And Release

Integrated into `develop`: pending.
Released through `main`: pending.

## 6. Risks and Mitigations

- *Risk*: An author edits the `packages` section by hand and the next run
  overwrites it.
  *Mitigation*: The generated comment at the top of the file says which part is
  generated, and the change shows up in review.
- *Risk*: A package is released without rerunning the generator.
  *Mitigation*: The validator fails `task check` until the manifest matches.
