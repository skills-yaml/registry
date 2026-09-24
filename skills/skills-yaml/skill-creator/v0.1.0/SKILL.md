---
name: skill-creator
description: Author a new skill package for a skills-yaml registry so it passes the registry gates on the first attempt. Use when adding a skill, packaging an existing prompt or workflow as a skill, publishing a new version of one, or fixing a package that CI rejected for structure, frontmatter, symlink or payload errors.
metadata:
  skm-version: "0.1.0"
---

# Skill Creator

A registry package is not just a `SKILL.md`. It is a versioned directory with a
duplicated root payload, two contained symlinks, and frontmatter that has to
satisfy every agent that will load it. Getting one of those wrong is the normal
failure, and the validator catches it after the work rather than during.

Build the package in the order below and the gates pass the first time.

## When to use

- Adding a new skill to a registry.
- Turning an existing prompt, checklist or runbook into a skill package.
- Publishing a new version of a skill that already exists.
- Repairing a package CI rejected.

## Before writing anything

Read the authoritative documents in the target registry. They govern; this skill
only puts the sequence in your hands:

- `SKILL_STRUCTURE.md` — layout and frontmatter requirements
- `VERSIONING.md` — versions, aliases, publishing and withdrawal
- `README.md` — the catalog and contribution steps
- `scripts/validate_registry.py` — what actually fails, when the prose is unclear

If the registry practises spec-driven development, write the spec first and get
it into the development state. Do not start the package before the spec records
scope, acceptance criteria, affected areas and validation gates.

## Workflow

### 1. Choose the namespace and name

Pick an existing namespace when one fits. The name is kebab-case, 1–64
characters, and **must equal the directory name** — OpenCode enforces this and
the validator does too. Lowercase alphanumeric with single hyphens, no leading,
trailing or doubled hyphen.

### 2. Write `SKILL.md`

Frontmatter carries `name`, `description`, and registry values as strings under
`metadata`:

```yaml
---
name: my-skill
description: One or two sentences on what it does and when to use it.
metadata:
  skm-version: "0.1.0"
---
```

`skm-version` is how newly published packages declare their version. A top-level
`version` string is the legacy form; do not use it for a new package.

Write the description for a machine deciding whether to load the skill. State
what it does and the situations that should trigger it. Keep it under 1024
characters — the limit that binds first across agents.

The body is instructions for an agent, not documentation for a reader. Lead with
what to do. Put long reference material in `references/` and link it, so the
agent loads it only when needed.

### 3. Build the version directory

```text
skills/<namespace>/<name>/
├── SKILL.md          # identical to the copy in v0.1.0
├── latest -> v0.1.0
├── default -> v0.1.0
└── v0.1.0/
    ├── SKILL.md
    ├── references/   # optional
    ├── templates/    # optional
    ├── scripts/      # optional, executable
    └── assets/       # optional
```

Assemble the version directory first, then copy its payload to the root. They are
compared byte for byte, including file modes, so copy rather than retype:

```bash
cp -a v0.1.0/SKILL.md v0.1.0/references .
ln -s v0.1.0 latest
ln -s v0.1.0 default
```

Aliases must be relative, contained, and point at a real exact-version directory.
`latest` must target the highest published version.

### 4. Check the links resolve twice

Every relative link in `SKILL.md` must resolve from the root payload **and** from
the version directory, because both copies are installed. A link that works only
in one place is the most common defect: see `references/package-layout.md`.

Scripts need the executable bit in both copies. `cp -a` preserves it.

### 5. Declare dependencies, if any

```yaml
metadata:
  skm-dependencies: "namespace/other-skill@1.2.0, namespace/third@0.3.0"
```

Exact versions only, from the same registry, comma-and-space separated, no
duplicates, and the graph must stay acyclic. Ranges, aliases and paths are
rejected.

### 6. Update the catalog and validate

Add the skill to the README catalog. Then run the registry's gates — typically
`task check` and `task test` — and fix what they report before opening a pull
request. Record in the spec which gates ran and any that were skipped, with the
reason.

## Publishing a new version

Never edit a published exact version. Once it reaches the production branch its
paths, modes and bytes are frozen. To change a released skill, add a new version
directory, move `latest` and the root payload to it, and leave the old directory
in place for consumers pinned to it.

A release that must not stay published is withdrawn, not edited: remove the
directory and record it in the registry's withdrawal ledger with a date and a
reason. Withdrawal does not erase anything from history.

Choose the number by what changed for a consumer, not by effort. A change to what
the skill tells an agent to do is at least a minor release.

## Support files

- **Package layout and the rules that catch people**: `references/package-layout.md`
- **Frontmatter that works in every agent**: `references/frontmatter-contract.md`
- **Starting point for a new skill**: `templates/SKILL.md.template`
