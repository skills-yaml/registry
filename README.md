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

### Workspace lifecycle

The `workspace` namespace publishes 19 independently versioned packages from
Workspace toolkit 0.3.0. Focused packages can be installed directly. The seven
public lifecycle facades preserve the conceptual `wk.*` vocabulary while using
portable kebab-case package and invocation names:

| Concept | Registry package | Direct invocation |
| --- | --- | --- |
| `wk.adopt` | `workspace/wk-adopt` | `$wk-adopt` |
| `wk.analyze` | `workspace/wk-analyze` | `$wk-analyze` |
| `wk.document` | `workspace/wk-document` | `$wk-document` |
| `wk.spec` | `workspace/wk-spec` | `$wk-spec` |
| `wk.plan` | `workspace/wk-plan` | `$wk-plan` |
| `wk.deliver` | `workspace/wk-deliver` | `$wk-deliver` |
| `wk.review` | `workspace/wk-review` | `$wk-review` |

For example, `workspace/wk-deliver@0.1.0` declares exact dependencies on its
focused planning, implementation, review, security, CI, and remediation skills.
SKM 0.4.0 or later resolves that dependency closure and installs Codex skills
under `.agents/skills/`.

Use exact versions for reproducible automation:

```yaml
skills:
  - name: workspace/wk-spec
    version: "0.1.0"
```

`skills/workspace/manifest.yaml` is the release-set ledger for the namespace.
Each package also carries its own canonical source revision, source path,
source integrity, compatibility, and exact dependency metadata.

Schema-2 namespace manifests may also publish named bundles. The planned
`workspace/all-workspace-skills` bundle lists every current Workspace package
once and installs no additional skill. A compatible SKM adds its exact members
with `skm bundle add workspace/all-workspace-skills --source default --yes`.
This bundle is pending a released Workspace source and Registry review; the
currently published Workspace manifest remains schema 1.

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
