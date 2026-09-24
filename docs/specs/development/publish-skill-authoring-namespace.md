# Spec: Publish The `skills-yaml` Authoring Namespace

Status: Development

Purpose: Publish the two skills that let an agent author and review registry
packages correctly, plus a meta package that installs both.

## 1. Problem Statement

The rules a registry package must satisfy are spread across `SKILL_STRUCTURE.md`,
`VERSIONING.md`, `README.md`, `WITHDRAWN.yaml` and `scripts/validate_registry.py`.
An agent asked to add a skill has to find and reconcile all of them, and the
evidence is that they do not: every skill contributed so far arrived with defects
that CI later rejected. `gcp-debug` shipped a root payload missing its
`references/` directory, so the root `SKILL.md` linked a file that did not exist
beside it; it declared a `workspace-docs` version this repository never adopted;
and it credited an author who never contributed here.

Review has the same gap from the other side. Nothing states what a reviewer
checks, and skills carry executable scripts. `devops-manager` ships three shell
scripts that read `/var/log/auth.log`, enumerate listening ports and inspect
firewall rules. Those are legitimate for that skill, but no one wrote down how to
tell a legitimate one from a malicious one, and a skill is instructions an agent
will follow with the user's privileges.

## 2. Goals and Non-Goals

### Goals

- Publish `skills-yaml/skill-creator`: how to author a package that passes the
  gates on the first attempt.
- Publish `skills-yaml/skill-reviewer`: how to review a package for compliance,
  and for unsafe or malicious behavior in its scripts and its instructions.
- Publish `skills-yaml/authoring-toolkit`: a meta package that installs both
  through `skm-dependencies` and carries no instructions of its own.
- Keep all three inside the portability baseline, so they work in every agent
  the ecosystem supports.

### Non-Goals

- Automating review. The reviewer skill is a procedure for an agent to follow,
  not a scanner. `task check` remains the mechanical gate.
- Duplicating `SKILL_STRUCTURE.md` or `VERSIONING.md`. The skills point at those
  documents as the source of truth and carry only what an author needs in hand.
- Sandboxing or executing skill scripts. The reviewer reads them; it does not run
  them, and says so explicitly.

## 3. Proposed Design

A new namespace, `skills-yaml`, holding three packages at `0.1.0`:

```
skills/skills-yaml/
├── skill-creator/      SKILL.md + references/ + templates/
├── skill-reviewer/     SKILL.md + references/
└── authoring-toolkit/  SKILL.md only; depends on the other two
```

Each follows the published layout: a root payload identical to `latest`, an
exact `v0.1.0/` directory, and contained `latest` and `default` symlinks.

The meta package declares:

```yaml
metadata:
  skm-version: "0.1.0"
  skm-dependencies: "skills-yaml/skill-creator@0.1.0, skills-yaml/skill-reviewer@0.1.0"
```

`skm` 0.4.0 and later resolves the transitive closure, so installing the toolkit
installs both skills. Its description states that it is a bundle, so an agent
scanning descriptions does not invoke it expecting instructions.

### Why a namespace rather than adding to `system`

These packages are about this registry's own contract. Grouping them under the
project name keeps that visible and leaves room for further authoring tools
without diluting a functional category.

### Portability

All three stay within `name` plus `description` and a string `metadata` map. No
agent-specific frontmatter. Names are kebab-case and match their directories;
descriptions stay under 1024 characters, the limit that binds first.

## 4. Verification and Acceptance Criteria

- [x] Three packages exist under `skills/skills-yaml/` with root payloads
      matching `v0.1.0` exactly. The validator's root/current comparison covers
      this.
- [x] `latest` and `default` resolve to `v0.1.0` in each.
- [x] The meta package's dependencies resolve to published coordinates and the
      graph stays acyclic; the dependency check passes.
- [x] Every relative link in every `SKILL.md` resolves from both the root payload
      and the version directory, checked from both locations.
- [x] Frontmatter uses `metadata.skm-version`; no agent-specific field appears in
      any of the three. Names are 13 to 17 characters, descriptions 248 to 359,
      against limits of 64 and 1024.
- [x] The README catalog lists the namespace.
- [x] `task check` passes: 25 packages, 25 exact releases, immutability clean
      against `origin/main`. `task test`: 18 tests.

## 6. Integration And Release

Integrated into `develop`: pending.
Released through `main`: pending. This spec stays in `development` until the
release event is confirmed, per the branch model in `AGENTS.md`.

## 5. Risks and Mitigations

- *Risk*: The skills drift from the documents they describe, and an agent follows
  stale rules confidently.
  *Mitigation*: Each skill cites the authoritative document per rule rather than
  restating it, so drift shows up as a broken citation. A change to
  `SKILL_STRUCTURE.md`, `VERSIONING.md` or the validator is the trigger to
  republish.
- *Risk*: The reviewer skill reads as a security guarantee.
  *Mitigation*: It states plainly that it is a structured reading of a package by
  a fallible reviewer, that it never executes what it reviews, and that a clean
  review is not proof of safety.
- *Risk*: The meta package is invoked by a model expecting instructions.
  *Mitigation*: Its description says it installs the other two and contains no
  procedure.
