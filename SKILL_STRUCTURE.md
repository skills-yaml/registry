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

The `SKILL.md` file must start with YAML frontmatter containing:

```yaml
---
name: <skill-name>              # REQUIRED: Short identifier (kebab-case, no spaces)
description: "<description>"    # REQUIRED: One-sentence description of purpose
tags:                          # OPTIONAL: List of tags for categorization
  - <tag1>
  - <tag2>
version: "0.1.0"               # OPTIONAL: Version (defaults to "latest")
authors:                       # OPTIONAL: List of contributors
  - "Author Name <email>"
---
```

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

---

## 🔗 Linking to Root README

The root `README.md` file links to this document as the authoritative specification for skill structure. See the [Registry README](../README.md) for the high-level overview.

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
tags:
  - code-quality
  - review
version: "0.1.0"
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
3. **Path** must be resolvable (no symlinks, no special characters)
4. **Name** must pass validation (kebab-case, no `..`, no absolute paths)

The `skm check` command verifies all these requirements.
