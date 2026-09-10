# Skill Structure Specification

This document defines the **standard structure** for all skills in the registry. Every skill must follow this format to be compatible with the `skm` tool.

---

## 📁 Directory Structure

```
registry/
├── skills/
│   └── <category>/
│       └── <skill-name>/
│           ├── SKILL.md          # REQUIRED: Skill manifest and documentation
│           ├── references/       # OPTIONAL: Supporting documents, checklists, recipes
│           │   └── *.md
│           ├── templates/        # OPTIONAL: Reusable templates and scaffolds
│           │   └── *.md
│           ├── scripts/          # OPTIONAL: Executable helper scripts
│           │   └── *.sh
│           └── assets/            # OPTIONAL: Static files, diagrams, etc.
│               └── *
└── agents/                     # Future: Agent-specific configurations
```

---

## 📄 Required Files

### `SKILL.md` (Mandatory)

Every skill **MUST** have a `SKILL.md` file at its root. This file serves as both the skill's manifest (for `skm` to recognize it) and its primary documentation.

#### Frontmatter (YAML)

The `SKILL.md` file must start with Agent Skills-compatible YAML frontmatter.
New packages should put registry-specific scalar values in the `metadata` map:

```yaml
---
name: <skill-name>              # REQUIRED: Short identifier (kebab-case, no spaces)
description: "<description>"    # REQUIRED: One-sentence description of purpose
metadata:
  skm-version: "0.1.0"         # REQUIRED for newly published versions
  skm-dependencies: "category/other-skill@1.2.3" # OPTIONAL
---
```

All keys and values under `metadata` must be strings. Existing legacy packages
may retain a top-level string `version`; newly published packages use
`metadata.skm-version` so their frontmatter remains portable across Agent Skills
consumers.

Dependencies are a canonical comma-and-space-separated list of exact package
coordinates from the same trusted registry. Ranges, aliases, local paths, and
URLs are not accepted. Dependency graphs must resolve completely and must not
contain cycles.

### Workspace provenance metadata

Every package in the `workspace` namespace additionally declares these string
metadata keys:

- `skm-source-repository`
- `skm-source-revision`
- `skm-source-path`
- `skm-source-integrity`
- `workspace-toolkit-version`
- `workspace-docs-compatibility`
- `minimum-skm-version`
- `skm-adapter-compatibility`

The namespace manifest at `skills/workspace/manifest.yaml` must exactly list
the current package versions and agree with their shared source and compatibility
metadata.

#### Skill Name Rules

- Must be **kebab-case** (lowercase, hyphens only)
- No spaces, underscores, or special characters
- Must match the directory name
- Examples: `spec`, `devops-manager`, `code-review`

#### Content Sections

The body of `SKILL.md` should include:

1. **# <Skill Name>** - Title (H1)
2. **Short description** - One paragraph explaining the skill's purpose
3. **When to use** - Bullet list of scenarios where this skill should be activated
4. **Core principles/workflows** - Main functionality and approach
5. **Support files** - Links to files in subdirectories (references/, templates/, etc.)

See existing skills (`spec`, `devops-manager`) for examples.

---

## 📂 Optional Directories

### `references/`

Contains supporting documentation, checklists, and reference materials.

- Use for: In-depth guides, recipes, recipes, cheat sheets
- Files: `.md` format
- Example: `references/spec-writing-checklist.md`

**Naming convention:** Use kebab-case for files, e.g., `my-reference.md`

### `templates/`

Contains reusable scaffolds and templates.

- Use for: Boilerplate code, document templates, configuration examples
- Files: Any format (`.md`, `.yaml`, `.json`, `.txt`, etc.)
- Example: `templates/spec-template.md`

### `scripts/`

Contains executable helper scripts.

- Use for: Automated checks, setup scripts, validation tools
- Files: Executable scripts (`.sh`, `.py`, etc.)
- **Requirement:** Scripts must have executable permissions (`chmod +x`)
- Example: `scripts/health.sh`

### `assets/`

Contains static files and resources.

- Use for: Diagrams, images, configuration files, sample data
- Files: Any format
- Example: `assets/architecture-diagram.png`

---

## 🏷️ Categorization

Skills are organized by **category** in the `skills/` directory:

```
skills/
├── software-development/   # Coding, design, architecture
│   ├── spec/
│   └── code-review/
├── system/                # System administration, DevOps
│   └── devops-manager/
├── data/                  # Data processing, analytics
├── security/              # Security practices, auditing
├── project-management/    # Planning, tracking
└── ...
```

**Category rules:**
- Use **plural, lowercase** names (e.g., `software-development`, not `SoftwareDevelopment`)
- Group related skills together
- Avoid creating too many top-level categories

---

## 📋 Skill Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Category | kebab-case, plural | `software-development` |
| Skill name | kebab-case, singular | `spec` |
| Directory | matches skill name | `skills/software-development/spec/` |
| Files | kebab-case | `spec-writing-checklist.md` |

---

## ✅ Validation Checklist

Before adding a skill to the registry, verify:

- [ ] `SKILL.md` exists at the skill root
- [ ] `SKILL.md` has valid YAML frontmatter with `name` and `description`
- [ ] Skill name matches directory name
- [ ] Skill name is kebab-case
- [ ] Category directory exists and is appropriately named
- [ ] All referenced files in `SKILL.md` exist
- [ ] Scripts in `scripts/` are executable (`chmod +x`)
- [ ] Exact version directories are real directories and have not been modified
- [ ] `latest` and `default` are contained symlinks to real exact versions
- [ ] The root/current payload exactly matches the `latest` version
- [ ] Exact dependencies resolve and the graph is acyclic
- [ ] Required provenance and integrity metadata validates
- [ ] `task check` passes

---

## 🔗 Linking to Root README

The root `README.md` file links to this document as the authoritative specification for skill structure. See the [Registry README](./README.md) for the high-level overview.

---

## 📝 Example: Creating a New Skill

To add a new skill called `code-review` in the `software-development` category:

```bash
# 1. Create the directory structure
mkdir -p skills/software-development/code-review/references

# 2. Create SKILL.md with frontmatter
cat > skills/software-development/code-review/SKILL.md << 'EOF'
---
name: code-review
description: "Perform thorough code reviews with focus on correctness, performance, and maintainability."
metadata:
  skm-version: "0.1.0"
---

# Code Review

Perform comprehensive code reviews...
EOF

# 3. Add supporting files (optional)
cat > skills/software-development/code-review/references/checklist.md << 'EOF'
# Code Review Checklist

- [ ] Functionality...
EOF

# 4. Test locally
cd /path/to/project
skm init
# Edit skills.yaml to include the new skill
skm install
```

---

## 🔒 Requirements for `skm` Compatibility

For a skill to be correctly linked by `skm`:

1. **Directory name** must be the same as the `name` in `SKILL.md` frontmatter
2. **`SKILL.md`** must exist at the skill's root directory
3. **Payload paths and exact version directories** must be real, contained paths;
   only the package-root `latest` and `default` aliases may be symlinks
4. **Name** must pass validation (kebab-case, no `..`, no absolute paths)

The `skm check` command verifies all these requirements.
