# The `workspace` Namespace

The `workspace` namespace publishes the skills of the
[Workspace toolkit](https://github.com/skills-yaml/workspace). They are
ordinary registry packages: skm installs them like any other skill, and
nothing in skm or `skills.yaml` requires them.

## Packages

The namespace holds 20 independently versioned packages. Focused packages can
be installed directly. The seven public lifecycle facades preserve the
conceptual `wk.*` vocabulary while using portable kebab-case package and
invocation names:

| Concept | Registry package | Direct invocation |
| --- | --- | --- |
| `wk.adopt` | `workspace/wk-adopt` | `$wk-adopt` |
| `wk.analyze` | `workspace/wk-analyze` | `$wk-analyze` |
| `wk.document` | `workspace/wk-document` | `$wk-document` |
| `wk.spec` | `workspace/wk-spec` | `$wk-spec` |
| `wk.plan` | `workspace/wk-plan` | `$wk-plan` |
| `wk.deliver` | `workspace/wk-deliver` | `$wk-deliver` |
| `wk.review` | `workspace/wk-review` | `$wk-review` |

A facade declares exact dependencies on the focused skills it drives. For
example, `workspace/wk-deliver` depends on its planning, implementation,
review, security, CI, and remediation skills. SKM 0.4.0 or later resolves that
dependency closure and installs Codex skills under `.agents/skills/`.

Use exact versions for reproducible automation. The current version of each
package is listed in `skills/workspace/manifest.yaml`:

```yaml
skills:
  - name: workspace/wk-spec
    version: "0.2.1"
```

To add every package at once, use the `workspace/all-workspace-skills` bundle:

```sh
skm add workspace/all-workspace-skills --source default --kind bundle --dry-run
skm add workspace/all-workspace-skills --source default --kind bundle --yes
```

## Adopting Workspace Docs

SKM 0.7.0 has no `skm workspace` command. For Workspace Docs assessment,
adoption, upgrade or repair, add the `workspace/wk-adopt` skill with
`skm add workspace/wk-adopt --source default` and invoke it in your agent.

## Provenance

`skills/workspace/manifest.yaml` is the release-set ledger for the namespace.
It records the toolkit version, source repository and revision, Workspace Docs
compatibility, and the minimum SKM version. Each package also carries its own
canonical source revision, source path, source integrity, compatibility, and
exact dependency metadata.

The Workspace packager generates the manifest and every package in this
namespace. Do not hand-edit generated root copies or exact version directories.
`task manifest` leaves this namespace unchanged, and the registry validator
checks its provenance fields.
