# Registry

Central registry of versioned skills and agents for the SKM ecosystem.

## Structure

For the complete skill structure specification, see [SKILL_STRUCTURE.md](./SKILL_STRUCTURE.md).

## Versioning

For versioning rules and best practices for skills and agents, see [VERSIONING.md](./VERSIONING.md).

```
registry/
├── skills/
│   ├── software-development/
│   │   └── spec/          # Spec writing skill
│   │       ├── SKILL.md
│   │       ├── latest -> v1.0.0    # Symlink to latest
│   │       ├── default -> v1.0.0   # Symlink to default
│   │       └── v1.0.0/    # Pinned version
│   ├── system/
│   │   └── devops-manager/ # System monitoring and management
│   │       ├── SKILL.md
│   │       ├── latest -> v1.0.0
│   │       ├── default -> v1.0.0
│   │       └── v1.0.0/
│   └── workspace/
│       ├── manifest.yaml # Workspace release-set manifest
│       └── wk-spec/      # Explicit Workspace lifecycle facade
│           ├── SKILL.md
│           ├── latest -> v0.1.0
│           ├── default -> v0.1.0
│           └── v0.1.0/
└── agents/
    └── claude/         # Agent integration
        └── MANIFEST.md
```

## Skills

### Software Development
- **spec** - Write clear, reviewable software specs with Symphony-style structure

### System
- **devops-manager** - Manage system services, health, security, and updates on Debian/Docker machines
- **gcp-debug** - Debug GCP services with Cloud Logging queries and status checks across Cloud Run, Cloud Functions, GKE and Compute Engine

### Skills-yaml

Authoring tools for this registry's own contract.

- **skill-creator** - Author a skill package that passes the registry gates on the first attempt
- **skill-reviewer** - Review a package for registry compliance, then for unsafe or malicious behavior in its scripts and instructions

### Workspace

Skills from the [Workspace toolkit](https://github.com/skills-yaml/workspace),
including the seven `wk-*` lifecycle facades such as `workspace/wk-spec` and
`workspace/wk-deliver`. See [docs/namespaces/workspace.md](./docs/namespaces/workspace.md)
for the package list, provenance rules, and Workspace Docs adoption.

## Bundles

Schema-2 namespace manifests can publish named bundles, which are groups
of skills that are offered together. Two bundles are published today:
`workspace/all-workspace-skills`, which contains every current Workspace
package, and `skills-yaml/authoring-toolkit`, which contains `skill-creator` and
`skill-reviewer`. A bundle installs no extra skill of its own. With SKM 0.7.0 or
later, you can preview a bundle and then add its skills to your project:

```sh
skm add skills-yaml/authoring-toolkit --source default --kind bundle --dry-run
skm add skills-yaml/authoring-toolkit --source default --kind bundle --yes
```

`skm bundle add skills-yaml/authoring-toolkit --source default --yes` does the
same thing. SKM writes each member into `skills.yaml` as a separate entry pinned
to an exact version.

`skm search <query>` lists skills and bundles from your registries in one
result list, with the `skm add` command for each result. It never changes your
project.

To publish a bundle in a namespace you maintain by hand, write only the
`bundles` section of `skills/<namespace>/manifest.yaml` and run `task manifest`.
The command fills in the rest of the file from the package folders, so you never
have to copy version numbers into it yourself. Run it again whenever you publish
a new version of a package in that namespace; `task check` fails if the manifest
is out of date.

## Adding New Skills

See [SKILL_STRUCTURE.md](./SKILL_STRUCTURE.md) for complete requirements.
See [VERSIONING.md](./VERSIONING.md) for versioning rules.

Quick start for an independently authored package:
1. Add your skill directory: `skills/<category>/<skill-name>/`
2. Create `SKILL.md` with `metadata.skm-version` in frontmatter
3. Create version directory: `skills/<category>/<skill-name>/v1.0.0/`
4. Copy skill files into version directory
5. Create symlinks: `latest -> v1.0.0` and `default -> v1.0.0`
6. Update this README with the new skill description
7. Run `task check`
8. Commit and push to GitHub

Generated Workspace packages must be produced by the revision-verifying
Workspace packager. Do not hand-edit generated root copies or exact version
directories in this repository.

## Validation

```bash
task check
task test
task registry:check
```

Registry validation is deterministic and offline. It checks package identity,
aliases, root/version equivalence, exact dependencies, Workspace provenance and
source integrity, path containment, and the immutability of versions already
published on `origin/main`.

Example for new skill at v1.0.0:
```bash
mkdir -p skills/my-category/my-skill/v1.0.0
# Create SKILL.md with metadata.skm-version: "1.0.0"
cp -r my-files/* skills/my-category/my-skill/v1.0.0/
cd skills/my-category/my-skill
ln -s v1.0.0 latest
ln -s v1.0.0 default
```

## License

All skills are open source and available for use with skm.
