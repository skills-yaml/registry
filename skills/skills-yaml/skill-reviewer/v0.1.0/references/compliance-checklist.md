# Compliance Checklist

Work top to bottom. Items marked *gate* are enforced by
`scripts/validate_registry.py`; the rest need a human or agent to look.

## Structure

- [ ] *gate* Package is a real directory under a kebab-case namespace.
- [ ] *gate* At least one exact `vX.Y.Z/` directory exists, as a real directory.
- [ ] *gate* `latest` and `default` are symlinks to one contained version
      directory, with no slashes or `..` in the target.
- [ ] *gate* `latest` targets the highest published semantic version.
- [ ] *gate* Root payload matches the `latest` version byte for byte, including
      file modes.
- [ ] *gate* No symlinks inside a payload; at most 256 files and 10 MB.
- [ ] Scripts carry the executable bit in **both** copies.

## Frontmatter

- [ ] *gate* Valid YAML, no duplicate keys.
- [ ] *gate* `name` equals the directory name.
- [ ] *gate* `description` is a non-empty string, at most 1024 characters.
- [ ] *gate* An exact semantic version is declared, through
      `metadata.skm-version` for a new package.
- [ ] *gate* Everything under `metadata` is a string.
- [ ] `name` is at most 64 characters.
- [ ] No agent-specific fields: `allowed-tools`, `icon`, `color`, `paths`,
      `globs`, `disable-model-invocation`, `user-invocable`, `context`, `model`.

## Dependencies

- [ ] *gate* `skm-dependencies` is a canonical comma-and-space list of exact
      coordinates, with no duplicates.
- [ ] *gate* Every coordinate is published in the same registry.
- [ ] *gate* The dependency graph is acyclic.

## Versioning

- [ ] *gate* No published exact version was edited or deleted.
- [ ] A removed version is recorded in the withdrawal ledger with a date and a
      reason.
- [ ] The version bump matches what changed for a consumer: behavior change is
      at least a minor release; a fix that leaves instructions the same is a
      patch.

## Content

- [ ] The description states when to trigger, not only what the skill is.
- [ ] The body matches what the description promises — no undisclosed extra
      capability.
- [ ] Every relative link resolves from the root payload **and** the version
      directory.
- [ ] Referenced support files exist and are reachable.
- [ ] No machine-specific content: real hostnames, internal service names, port
      inventories, absolute paths under a user's home, personal email addresses.
- [ ] No credentials, tokens or connection strings, in any file.
- [ ] Attribution is accurate. Do not credit an author or organization that did
      not contribute.

## Catalog and process

- [ ] The registry catalog lists the skill.
- [ ] A spec covers the change and is in the right lifecycle state.
- [ ] Validation gates were run and recorded, with reasons for any skipped.
