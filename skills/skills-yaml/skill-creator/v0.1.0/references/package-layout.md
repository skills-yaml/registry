# Package Layout And The Rules That Catch People

Every rule here is enforced by `scripts/validate_registry.py`. The failure text
is quoted so you can search for it when CI rejects a package.

## The root payload must match `latest` exactly

> `root/current payload must exactly match the latest version`

The package root carries a second copy of the latest version's payload:
`SKILL.md` and every support directory. The comparison covers relative paths,
file contents and the executable bit.

Consequences people hit:

- Copying `SKILL.md` to the root but not `references/` leaves the root's links
  broken. This is what `gcp-debug` shipped: the root `SKILL.md` linked
  `references/gcloud-cheatsheet.md`, which existed only under `v0.1.0/`.
- Editing one copy and not the other fails the comparison.
- Recreating a script rather than copying it can lose the executable bit.

Use `cp -a` from the version directory to the root, and redo it after any edit.

## Both copies are installed, so links must resolve from both

A consumer may resolve `latest`, `default`, or an exact version. The root copy is
used for discovery. A relative link must therefore resolve from the package root
and from `v<version>/`. Keep support files in the same relative position in both,
which the payload rule already forces.

## Aliases are contained relative symlinks

> `alias must target one contained exact version directory`

`latest` and `default` are symlinks whose target is a single path segment such as
`v1.2.0` — no slashes, no `..`, no absolute paths, and the target must be a real
directory inside the package. `latest` must point at the highest published
semantic version. `default` may lag deliberately when the newest release is not
yet recommended.

## Names

> `frontmatter name must be <skill_id>`

The frontmatter `name` equals the directory name. Kebab-case: lowercase
alphanumeric with single hyphens, no leading, trailing or consecutive hyphen.
Keep it to 64 characters — some agents reject longer names even where the
registry currently accepts them.

Namespaces follow the same character rules.

## Published versions are immutable

> `published exact versions are immutable relative to origin/main`

Once an exact version directory reaches the production branch, its paths, file
types, modes and bytes are frozen. The check compares the full set of published
entries, so this rejects edits **and** deletions. Corrections require a new
version.

The only way to remove a published version is a declared withdrawal: delete the
directory and record the coordinate, a date and a reason in the registry's
withdrawal ledger. A withdrawal does not remove anything from Git history; treat
whatever the release disclosed as public.

## Size and shape limits

- At most 256 files and 10 MB per package payload.
- Regular files and directories only inside a version directory. No symlinks
  within the payload; the alias symlinks live at the package root.
- Scripts that are meant to run need the executable bit, in both copies.

## Dependencies

> `invalid exact dependency coordinate`

`metadata.skm-dependencies` is a single string: exact `namespace/name@version`
coordinates, separated by a comma and one space, no duplicates. Every coordinate
must already be published in the same registry, and the resulting graph must be
acyclic.

## Frontmatter is YAML with unique keys

The validator parses frontmatter with a loader that rejects duplicate mapping
keys and non-scalar keys. Everything under `metadata` must be a string — quote
version numbers and booleans.
