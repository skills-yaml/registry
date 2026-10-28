# The `workspace` Namespace

The `workspace` namespace publishes the skills of the
[Workspace toolkit](https://github.com/skills-yaml/workspace). They are
ordinary registry packages: skm installs them like any other skill, and
nothing in skm or `skills.yaml` requires them.

## Packages

The namespace holds 22 independently versioned packages (Toolkit `0.12.0`, Workspace Docs `8.x`, minimum SKM `0.7.0`). Focused packages can
be installed directly.
The public lifecycle facades preserve the
conceptual `wk.*` vocabulary while using portable kebab-case package and
invocation names:

| Concept | Registry package | Direct invocation |
| --- | --- | --- |
| `wk.adopt` | `workspace/wk-adopt` | `$wk-adopt` |
| `wk.analyze` | `workspace/wk-analyze` | `$wk-analyze` |
| `wk.deliver` | `workspace/wk-deliver` | `$wk-deliver` |
| `wk.document` | `workspace/wk-document` | `$wk-document` |
| `wk.plan` | `workspace/wk-plan` | `$wk-plan` |
| `wk.review` | `workspace/wk-review` | `$wk-review` |
| `wk.spec` | `workspace/wk-spec` | `$wk-spec` |

A facade declares exact dependencies on the focused skills it drives. For
example, `workspace/wk-deliver` depends on its planning, implementation,
review, security, CI, and remediation skills. SKM resolves that
dependency closure and installs Codex skills under `.agents/skills/`.

Use exact versions for reproducible automation. The current version of each
package is listed in `skills/workspace/manifest.yaml`:

```yaml
skills:
  - name: workspace/wk-spec
    version: "0.4.3"
```

### Current Package Versions

| Package | Version | Dependencies |
| --- | --- | --- |
| `workspace/address-review-feedback` | `0.4.7` | none |
| `workspace/adopt-workspace-structure` | `0.10.0` | none |
| `workspace/analyze-repository` | `0.4.3` | `workspace/design-domain-model@0.1.3` |
| `workspace/coordinate-multi-agent-development` | `0.2.7` | none |
| `workspace/design-domain-model` | `0.1.3` | none |
| `workspace/fix-bug` | `0.4.7` | none |
| `workspace/fix-ci` | `0.4.7` | none |
| `workspace/implement-spec` | `0.5.3` | `workspace/design-domain-model@0.1.3` |
| `workspace/maintain-project-docs` | `0.3.7` | none |
| `workspace/monitor-ci` | `0.4.7` | none |
| `workspace/plan-implementation` | `0.5.3` | `workspace/design-domain-model@0.1.3` |
| `workspace/report-repository-status` | `0.1.3` | none |
| `workspace/review-changes` | `0.5.3` | `workspace/design-domain-model@0.1.3` |
| `workspace/review-security` | `0.5.3` | `workspace/design-domain-model@0.1.3` |
| `workspace/wk-adopt` | `0.4.2` | `workspace/adopt-workspace-structure@0.10.0` |
| `workspace/wk-analyze` | `0.4.3` | `workspace/analyze-repository@0.4.3` |
| `workspace/wk-deliver` | `0.4.3` | `workspace/write-spec@0.6.1`, `workspace/plan-implementation@0.5.3`, `workspace/implement-spec@0.5.3`, `workspace/review-changes@0.5.3`, `workspace/review-security@0.5.3`, `workspace/monitor-ci@0.4.7`, `workspace/fix-ci@0.4.7`, `workspace/address-review-feedback@0.4.7`, `workspace/coordinate-multi-agent-development@0.2.7` |
| `workspace/wk-document` | `0.3.7` | `workspace/maintain-project-docs@0.3.7` |
| `workspace/wk-plan` | `0.4.3` | `workspace/write-spec@0.6.1`, `workspace/plan-implementation@0.5.3` |
| `workspace/wk-review` | `0.4.3` | `workspace/review-changes@0.5.3`, `workspace/review-security@0.5.3` |
| `workspace/wk-spec` | `0.4.3` | `workspace/write-spec@0.6.1` |
| `workspace/write-spec` | `0.6.1` | `workspace/design-domain-model@0.1.3` |

To add every package at once, use the `workspace/all-workspace-skills` bundle:

```sh
skm add workspace/all-workspace-skills --source default --kind bundle --dry-run
skm add workspace/all-workspace-skills --source default --kind bundle --yes
```

## Adopting Workspace Docs

SKM has no `skm workspace` command. For Workspace Docs assessment,
adoption, upgrade or repair, add the `workspace/wk-adopt` skill with
`skm add workspace/wk-adopt --source default` and invoke it in your agent.

## Provenance

`skills/workspace/manifest.yaml` is the release-set ledger for the namespace.
It records the toolkit version, source repository and revision, Workspace Docs
compatibility, and the minimum SKM version. Each package also carries its own
canonical source revision, source path, source integrity, compatibility, and
exact dependency metadata.

The Workspace packager generates the manifest, namespace documentation, and
every package in this namespace. Do not hand-edit generated root copies or
exact version directories. `task manifest` leaves this namespace unchanged,
and the registry validator checks its provenance fields.

## Guided Adoption

Guided adoption explains observed architecture/technology evidence and
tradeoffs, asks only material unanswered choices, and records agreed deferred
improvements as actionable, linked specs. Supplied answers are reused.
Optional deferral never waives required adoption gates, changes
assessment-only scope or authorizes runtime refactors.
