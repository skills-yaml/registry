# Spec: Add `gcp-debug` Skill to Registry

Status: Done
Purpose: Create an explicit, standard-compliant skill in the registry for debugging Google Cloud Platform (GCP) services using logs and interrogating status.

## 1. Problem Statement
Developers and operators troubleshooting GCP services (Cloud Run, GKE, Cloud Functions, Compute Engine, Pub/Sub, App Engine, etc.) often need a standard checklist, common workflows, reference gcloud command patterns, and troubleshooting steps to diagnose errors, identify latency, inspect IAM permissions, or check service health efficiently without memorizing complex gcloud flags or query syntax.

## 2. Goals and Non-Goals
### Goals
- Implement a `gcp-debug` skill in the `skills/system/` category.
- Adhere strictly to the `workspace-docs@1.0.0` / `registry` skill structural guidelines (explicit versioning structure under `v0.1.0/`, root `SKILL.md`, `latest` and `default` symlinks).
- Provide clear workflow instructions for:
  - Querying logs with Cloud Logging / `gcloud logging read`.
  - Interrogating status of various compute options (Cloud Run, Cloud Functions, GKE, GCE).
  - Verifying IAM, security policies, and service-to-service connectivity.
- Provide practical cheat sheets in `references/gcloud-cheatsheet.md`.

### Non-Goals
- Provide deep code-level application debugging details (e.g., Python/Go stack tracing).
- Install GCP SDK locally as part of the skill (it acts as guidance/instructions for agents).
- Integrate with AWS, Azure, or other cloud providers.

## 3. Proposed Design
We will place `gcp-debug` under `skills/system/gcp-debug/`:
```
skills/system/gcp-debug/
├── SKILL.md                          # Root payload, identical to the latest version
├── default -> v0.1.0/                # Symlink to stable
├── latest -> v0.1.0/                 # Symlink to latest
└── v0.1.0/
    ├── SKILL.md                      # Primary v0.1.0 manifest
    └── references/
        └── gcloud-cheatsheet.md     # Reference guides
```

The skill will contain:
1. `SKILL.md` with:
   - Frontmatter (name: `gcp-debug`, version: "0.1.0", description).
   - Core workflows: Cloud Logging interrogation (`gcloud logging`), Cloud Run status check, GKE cluster and pod status, Cloud Functions diagnostic, GCE instance health, IAM/Permission investigation, and common error recovery scenarios.
2. `references/gcloud-cheatsheet.md` containing real, copy-pasteable `gcloud` JSON queries, filtering syntaxes, status-interrogation commands, and IAM checks.

## 4. Verification and Acceptance Criteria
- [x] Directory structure is accurate.
- [x] Release declares `0.1.0` through `metadata.skm-version`, the form
      `SKILL_STRUCTURE.md` requires of newly published packages.
- [x] Directory name is kebab-case (`gcp-debug`) and matches the frontmatter name.
- [x] Symlinks `latest` and `default` point to `v0.1.0/`.
- [x] The root payload matches `v0.1.0` exactly, including `references/`.
- [x] `task check` and `task test` pass. The repository now has a Taskfile and
      CI, which this spec predates.

## 6. Notes

Two corrections made while completing this spec:

- The original frontmatter credited an author who did not write this skill, and
  carried a third party's email address. Removed.
- The spec claimed `workspace-docs@1.2.0`. The repository adopted `1.0.0`.

## 5. Risks and Mitigations
- *Risk*: Pinned version symlinks can be broken.
  *Mitigation*: Verify using native absolute/relative check paths or simple `ls -la` check.
