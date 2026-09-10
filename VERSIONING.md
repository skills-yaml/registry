# Versioning Specification

This document defines the **versioning scheme** for skills and agents in the registry. All versioned entities must follow this specification for compatibility with the `skm` tool.

---

## 📌 Overview

The registry supports versioning for:
- **Skills**: Individual skill packages with their own release cycles
- **Agents**: Agent-specific configurations and integrations

Versioning enables:
- Multiple versions of the same skill to coexist
- Rollback to previous versions
- Clear dependency management
- Reproducible environments

---

## 📦 Skill Versioning

### Version Format

Skills use **Semantic Versioning 2.0.0** (`MAJOR.MINOR.PATCH`):

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]
```

Examples:
- `1.0.0` - Stable release
- `1.0.0-alpha` - Alpha prerelease
- `1.0.0-beta.1` - Beta prerelease with build number
- `2.3.4` - Stable patch release
- `0.1.0` - Initial development version

### Version File Location

Skill versions are defined in two places:

1. **In `SKILL.md` frontmatter** (legacy form):
   ```yaml
   ---
   name: spec
   version: "1.2.3"
   description: "..."
   ---
   ```

   Newly published packages use the Agent Skills string metadata map:

   ```yaml
   ---
   name: spec
   description: "..."
   metadata:
     skm-version: "1.2.3"
   ---
   ```

2. **In `skills.yaml`** (consumer reference):
   ```yaml
   skills:
     - name: software-development/spec
       version: "1.2.3"
       source: default
   ```

### Version Resolution

When a skill is installed, `skm` resolves the version as follows:

1. If `version: "1.2.3"` → use exact pinned version from `v1.2.3/`
2. If `version: "latest"` → follow `latest/` symlink to newest version
3. If `version: "default"` → follow `default/` symlink to stable version
4. If `version` is omitted → same as `"latest"` (follow `latest/` symlink)

**Implementation:**
- `skm` checks if version is a symlink (`latest`, `default`) → follows it
- `skm` checks if version is exact (`v1.2.3`) → uses that directory
- `skm` checks if version is semver (`1.2.3`) → resolves to `v1.2.3/`

### Version Precedence

Versions are sorted using semantic version precedence:
- `1.0.0` < `1.0.1` < `1.1.0` < `2.0.0`
- Prereleases have lower precedence: `1.0.0` > `1.0.0-alpha`
- Build metadata is ignored for precedence: `1.0.0+20240101` == `1.0.0`

### Directory Structure with Versions

Skills with multiple versions are stored in an **explicit versioned directory structure** with symlinks for convenience:

```
registry/
└── skills/
    └── <category>/
        └── <skill-name>/
            ├── SKILL.md              # Metadata for latest version
            ├── latest -> v2.0.0      # Symlink: Always points to latest
            ├── default -> v1.0.0     # Symlink: Points to default/stable
            ├── v1.0.0/               # Pinned version 1.0.0
            │   ├── SKILL.md          # Version-specific metadata
            │   └── ...              # Version-specific files
            ├── v1.1.0/               # Pinned version 1.1.0
            │   ├── SKILL.md
            │   └── ...
            └── v2.0.0/               # Pinned version 2.0.0 (latest)
                ├── SKILL.md
                └── ...
```

**Key:**
- `latest` → **Symlink** to the newest version (resolves `latest` alias)
- `default` → **Symlink** to the recommended stable version (resolves `default` alias)
- `vX.Y.Z/` → **Pinned version** directories with actual files
- Root `SKILL.md` → Metadata for the latest version (used by `skm` for discovery)

The entire root/current payload must match the version selected by `latest`,
not only `SKILL.md`.

### Exact-version immutability

Once an exact `vMAJOR.MINOR.PATCH` directory reaches the production branch, its
paths, file types, executable modes, and bytes are immutable. Corrections require
a new semantic version. `task registry:check` compares published exact versions
with `origin/main` and rejects deletions, additions, or mutations inside them.

Alias targets and root/current copies may move forward to a newly added version,
but must remain contained within their package and internally consistent.

### Exact package dependencies

New packages may declare dependencies in `metadata.skm-dependencies`:

```yaml
metadata:
  skm-version: "0.1.0"
  skm-dependencies: "workspace/write-spec@0.2.0, workspace/review-changes@0.2.0"
```

SKM 0.4.0 and later resolves the transitive closure. Every coordinate must pin
an exact version in the same trusted registry, exist there, and participate in
an acyclic graph. Skills remain independently versioned; a bundle or release
manifest records a tested set without forcing lockstep version bumps.

### Version Aliases

The following aliases are **symlinks** in the skill directory:

| Alias | Symlink Target | Resolves To | Use Case |
|-------|----------------|-------------|----------|
| `latest` | `vX.Y.Z/` | Highest version | Default, development |
| `default` | `vX.Y.Z/` | Recommended stable | Production, CI |

**Note:** The `latest` and `default` symlinks are the supported aliases and must
exist in every skill directory. When a new version is released, update them to
contained, real exact version directories.

### Version Metadata in SKILL.md

Legacy `SKILL.md` frontmatter may include version-related top-level fields.
New packages keep registry values as strings under `metadata`:

```yaml
---
name: spec
description: "..."
metadata:
  skm-version: "2.0.0"
  deprecated: "false"
  replaces: "1.2.3"
---
```

### Version Selectors

SKM accepts exact versions plus the `latest` and `default` aliases in
`skills.yaml`. Version ranges and wildcards are not registry selectors.

```yaml
skills:
  # Exact version
  - name: software-development/spec
    version: "1.2.3"
    source: default

  # Latest version
  - name: software-development/spec
    version: "latest"
    source: default

  # Registry-selected stable default
  - name: software-development/spec
    version: "default"
    source: default
```

---

## 🤖 Agent Versioning

### Version Format

Agents also use Semantic Versioning, but with a different interpretation:

- **MAJOR**: Breaking changes to agent integration API
- **MINOR**: Backward-compatible new features
- **PATCH**: Bug fixes and minor improvements

### Agent Version File

Agent versions are defined in `agents/<agent-name>/MANIFEST.md`:

```yaml
---
name: claude
version: "1.0.0"
description: "Claude Code integration"
compatibilities:
  - ">=1.0.0"    # Compatible skill API versions
required_skills:
  - base
  - system
---
```

### Agent Compatibility

The `compatibilities` field specifies which skill API versions the agent supports. Skills must be compatible with the agent's requirements.

### Agent Directory Structure

```
registry/
└── agents/
    └── <agent-name>/
        ├── MANIFEST.md          # Agent metadata and version
        ├── config.yaml          # Default agent configuration
        └── integrations/        # Agent-specific integrations
            └── ...
```

### Agent-Skill Compatibility Matrix

| Agent Version | Skill API Version | Notes |
|---------------|-------------------|-------|
| 1.x.x | 1.x.x | Full compatibility |
| 2.x.x | 1.x.x | Backward compatible |
| 2.x.x | 2.x.x | New features available |

---

## 🔄 Version Management with skm

### Checking Available Versions

```bash
# List all available versions of a skill
skm versions software-development/spec

# Output:
# Available versions for software-development/spec:
#   2.0.0 (latest)
#   1.2.3
#   1.1.0
#   1.0.0
```

### Installing Specific Versions

```bash
# Add the skill at its default selector, then switch to an exact version
skm add software-development/spec
skm use software-development/spec@1.2.3 --yes

# Or pin `version: "1.2.3"` in skills.yaml and reconcile
skm install --yes
```

### Updating Skills

```bash
# Update a skill to its latest version
skm update-skill software-development/spec --yes

# Preview a switch to a specific version
skm use software-development/spec@2.0.0 --dry-run
```

### Lock File (`skills.lock.yaml`)

The `skm install` command generates `skills.lock.yaml` to pin resolved sources,
versions, integrity values, and adapter outputs. The lockfile is generated by
SKM and must not be edited manually.

```yaml
# skills.lock.yaml - Auto-generated, do not edit manually
schema_version: 1
skills:
  - id: software-development/spec
    version: "1.2.3"
    source: default
    integrity: sha256:abc123...
```

---

## 📊 Version Metadata in Registry

### Version Manifest (optional)

For complex versioning needs, a skill can include a `VERSIONS.md` file:

```markdown
# Version History

## 2.0.0 (2024-01-15)
- Added new spec template format
- Breaking: Changed checklist structure

## 1.2.3 (2023-12-01)
- Fixed typo in rewrite pattern
- Updated references

## 1.1.0 (2023-11-15)
- Added support for alternative formats

## 1.0.0 (2023-10-01)
- Initial release
```

### Changelog Format

Each version entry should include:
- Version number and date
- Summary of changes
- Breaking changes (if any)
- New features
- Bug fixes

---

## 🎯 Versioning Best Practices

### For Skill Authors

1. **Start at 0.1.0** for initial development
2. **Bump MAJOR** for breaking changes (API changes, structure changes)
3. **Bump MINOR** for backward-compatible new features
4. **Bump PATCH** for backward-compatible bug fixes
5. **Use prereleases** for experimental features (`-alpha`, `-beta`, `-rc`)
6. **Document breaking changes** clearly in release notes
7. **Maintain backward compatibility** within MAJOR versions when possible

### For Skill Consumers

1. **Pin versions** in production (`skills.lock`)
2. **Use ranges** in development for latest features
3. **Test updates** before deploying to production
4. **Monitor deprecation notices** in skill metadata

### For Agent Maintainers

1. **Version agent integrations** independently
2. **Declare compatibility** with skill API versions
3. **Test with multiple skill versions**
4. **Provide migration guides** for breaking changes

---

## 🔒 Version Validation Rules

`skm` enforces the following version validation:

- ✅ Valid semver format (MAJOR.MINOR.PATCH)
- ✅ Numeric only for MAJOR, MINOR, PATCH
- ✅ Optional prerelease identifiers (`-alpha`, `-beta.1`)
- ✅ Optional build metadata (`+20240101`)
- ❌ No leading zeros (except for `0.x.x`)
- ❌ No invalid characters
- ❌ No empty version strings

### Validation Examples

| Version | Valid | Reason |
|---------|-------|--------|
| `1.0.0` | ✅ | Standard semver |
| `0.1.0` | ✅ | Initial development |
| `2.3.4-alpha` | ✅ | Prerelease |
| `1.0.0+build123` | ✅ | Build metadata |
| `1.01.0` | ❌ | Leading zero in MINOR |
| `1.0` | ❌ | Missing PATCH |
| `1` | ❌ | Missing MINOR and PATCH |
| `latest` | ✅ | Special alias (resolved by skm) |
| `stable` | ✅ | Special alias (resolved by skm) |

---

## 🔧 Maintenance Workflow

### Releasing a New Version

When releasing version `v2.0.0` of a skill:

```bash
# 1. Create new version directory
mkdir -p skills/<category>/<skill-name>/v2.0.0

# 2. Copy files from previous version
cp -r skills/<category>/<skill-name>/v1.0.0/* skills/<category>/<skill-name>/v2.0.0/

# 3. Update SKILL.md in new version with new version
# Edit skills/<category>/<skill-name>/v2.0.0/SKILL.md

# 4. Update root SKILL.md to latest version
# Edit skills/<category>/<skill-name>/SKILL.md (version: "2.0.0")

# 5. Update symlinks
cd skills/<category>/<skill-name>
rm latest default
ln -s v2.0.0 latest
ln -s v2.0.0 default  # Or keep pointing to v1.0.0 for stability

# 6. Update VERSIONS.md with changelog
```

### Changing Default Version

To change which version is the default (e.g., keep v1.0.0 as default while v2.0.0 is latest):

```bash
cd skills/<category>/<skill-name>
rm default
ln -s v1.0.0 default  # Point default to stable version
ln -s v2.0.0 latest    # Point latest to newest version
```

This allows:
- `skm add my-skill --version latest` → gets v2.0.0
- `skm add my-skill --version default` → gets v1.0.0 (stable)
- `skm add my-skill --version 1.0.0` → gets v1.0.0 explicitly

---

## 📚 Related Documents

- [SKILL_STRUCTURE.md](./SKILL_STRUCTURE.md) - Skill directory structure and file requirements
- [README.md](./README.md) - Registry overview and skill catalog

---

## 🔄 Migration Guide

### From Unversioned to Versioned Skills

1. Audit existing skills and assign initial versions
2. Create versioned directories (`v1.0.0/`, `v1.1.0/`, etc.)
3. Update `SKILL.md` files with version metadata
4. Update `skills.yaml` references to include versions
5. Test with `skm check` and `skm install`

### Version Bump Process

1. Update version in `SKILL.md` frontmatter
2. Create new version directory if needed
3. Copy skill files to version directory
4. Update `VERSIONS.md` with changelog
5. Update root `SKILL.md` to latest version
6. Commit and tag the release
