---
name: authoring-toolkit
description: Meta package that installs the skills-yaml authoring set, skill-creator and skill-reviewer, together. It carries no instructions of its own; install it to get both skills, then use skill-creator to author a package and skill-reviewer to review one.
metadata:
  skm-version: "0.1.0"
  skm-dependencies: "skills-yaml/skill-creator@0.1.0, skills-yaml/skill-reviewer@0.1.0"
---

# Authoring Toolkit

This package installs the two skills that cover authoring and reviewing registry
packages. It contains no procedure. Use the skills it brings in:

- **`skills-yaml/skill-creator`** — author a package that passes the registry
  gates on the first attempt: layout, frontmatter, versions, aliases, the
  duplicated root payload, dependencies, and publishing a new version.
- **`skills-yaml/skill-reviewer`** — review a package in two passes: compliance
  against the registry contract, then safety, reading its scripts and its
  instructions for unsafe or malicious behavior without executing them.

## Installing

Add the toolkit to `skills.yaml` and `skm` resolves the dependencies:

```yaml
skills:
  - name: skills-yaml/authoring-toolkit
    version: 0.1.0
    source: default
```

Dependency resolution requires `skm` 0.4.0 or later. On an older version, add
`skills-yaml/skill-creator` and `skills-yaml/skill-reviewer` directly instead.

Install either skill on its own if you only need one; the toolkit exists so that
a project which authors and reviews skills declares one entry rather than two,
and stays on a matched pair of versions.
