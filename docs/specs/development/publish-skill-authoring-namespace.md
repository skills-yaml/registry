# Spec: Publish The `skills-yaml` Authoring Namespace

Status: Development

Purpose: Publish the two skills that let an agent author and review registry
packages correctly.

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
- Keep both inside the portability baseline, so they work in every agent
  the ecosystem supports.

### Non-Goals

- Automating review. The reviewer skill is a procedure for an agent to follow,
  not a scanner. `task check` remains the mechanical gate.
- Duplicating `SKILL_STRUCTURE.md` or `VERSIONING.md`. The skills point at those
  documents as the source of truth and carry only what an author needs in hand.
- Sandboxing or executing skill scripts. The reviewer reads them; it does not run
  them, and says so explicitly.
- Publishing a bundle of the two skills. See "Bundle deferred" below.

## 3. Proposed Design

A new namespace, `skills-yaml`, holding two packages at `0.1.0`:

```
skills/skills-yaml/
├── skill-creator/   SKILL.md + references/ + templates/
└── skill-reviewer/  SKILL.md + references/
```

Each follows the published layout: a root payload identical to `latest`, an
exact `v0.1.0/` directory, and contained `latest` and `default` symlinks.

### Bundle deferred

An earlier draft added a third package, `authoring-toolkit`: a `SKILL.md` with no
instructions that declared both skills in `skm-dependencies`. It was removed
before merge, for two reasons.

**It used a dependency to express a bundle.** A dependency states that one skill
needs another to function. A bundle states that several skills are offered
together. The two skills here do not need each other, so declaring them as
dependencies of a third package misstates the relationship.

**A skill with no instructions costs every agent.** It is indexed, listed as an
invocable skill, and may be loaded by a model expecting a procedure. Its
description could only ask the model not to use it.

The correct home is a namespace manifest bundle: named membership, no skill, no
dependency. The schema-2 manifest specified in
`backlog/publish-workspace-skill-bundles.md` provides exactly this, but only for
the `workspace` namespace. Generalizing it is a proposed amendment to that
specification and its SKM and Workspace companions. Once a generic manifest is
supported, the bundle is added as `skills/skills-yaml/manifest.yaml`.

Removing the package before merge avoids a withdrawal. Published versions are
immutable from the moment they reach `main`, so a package that should never have
existed would otherwise need a `WITHDRAWN.yaml` entry.

### Why a namespace rather than adding to `system`

These packages are about this registry's own contract. Grouping them under the
project name keeps that visible and leaves room for further authoring tools
without diluting a functional category.

### Portability

Both stay within `name` plus `description` and a string `metadata` map. No
agent-specific frontmatter. Names are kebab-case and match their directories;
descriptions stay under 1024 characters, the limit that binds first.

## 4. Verification and Acceptance Criteria

- [x] Two packages exist under `skills/skills-yaml/` with root payloads
      matching `v0.1.0` exactly. The validator's root/current comparison covers
      this.
- [x] `latest` and `default` resolve to `v0.1.0` in each.
- [x] Every relative link in each `SKILL.md` resolves from both the root payload
      and the version directory, checked from both locations.
- [x] Frontmatter uses `metadata.skm-version`; no agent-specific field appears in
      either. Names are 13 and 14 characters, descriptions 310 and 359,
      against limits of 64 and 1024.
- [x] The README catalog lists the namespace.
- [x] `task check` passes: 24 packages, 24 exact releases, immutability clean
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
- *Risk*: Users wanting both skills must add two entries until the generic
  bundle lands.
  *Mitigation*: Two entries is the normal case today, and the bundle will expand
  into exactly those two explicit entries when it arrives, so no configuration
  written now needs to change.
