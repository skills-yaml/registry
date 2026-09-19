# Spec: Remove Host Service Inventory From The Public Registry

Status: Done
Purpose: Remove the real service inventory of a private host from the public
`registry` repository, and keep the `devops-manager` skill useful without it.

## 1. Problem Statement

`skills/system/devops-manager/references/inventory.md`, published in both the
root payload and the released `v1.0.0` package, records the live configuration
of a specific machine: internal container names, the ports they listen on
(including a database port), and the public hostnames that route to each one.

The repository is public. Together those three facts are a map of the host's
attack surface: they name what is worth reaching, the port to reach it on, and
the hostname that resolves to it. The skill's own description
("on this Debian/Docker machine") also binds a reusable skill to one operator's
environment.

Nothing in the affected files is a credential. The exposure is infrastructure
disclosure, not secret disclosure.

## 2. Goals and Non-Goals

### Goals
- Remove every reference to real hostnames, service names and ports from the
  repository's current tree.
- Keep `devops-manager` installable and useful: replace the inventory with
  guidance on building one per host and keeping it out of public version control.
- Make the skill's description environment-neutral.
- Satisfy the repository gates, including released-version immutability.

### Non-Goals
- Rewriting Git history. The data stays in published commits after this change;
  that is tracked as a follow-up decision for the repository owner.
- Auditing the other skills. A repository-wide scan found no further hostnames,
  addresses, credentials or personal data.
- Changing `hostname-and-tailscale-naming.md`, which contains only generic
  procedure and no host identifiers.

## 3. Proposed Design

`scripts/validate_registry.py` holds published exact versions immutable against
`origin/main`: the affected `v1.0.0` files can be neither edited nor deleted, as
the check compares the full set of published entries. The repository therefore
had no way to retire a release that must not stay published, which is exactly
what this change needs.

So the gate gains a declared-withdrawal path, and the redaction uses it:

0. Add a root `WITHDRAWN.yaml` ledger and teach the validator about it. A
   withdrawal must name a version that exists in the base ref, carry a date and
   a reason, and its version directory must be gone from the tree. Immutability
   is unchanged for everything else: still no edits, and still no undeclared
   deletions.
1. Delete `skills/system/devops-manager/v1.0.0/` and record the withdrawal.
2. Publish `v1.1.0` containing the redacted payload:
   - `references/inventory.md` rewritten as instructions for building a host
     inventory, with no real service, port or hostname, and an explicit warning
     to keep it out of public repositories.
   - `SKILL.md` description and opening line made environment-neutral, and the
     inventory reference reworded.
   - `hostname-and-tailscale-naming.md` and the three scripts carried over
     unchanged.
3. Point `latest` and `default` at `v1.1.0` and sync the root payload to match it
   byte for byte, as the validator requires.

A minor version, not a patch: the inventory reference changes meaning, so a
consumer pinned to `1.0.0` should choose the move deliberately.

Withdrawal is the narrowest mechanism that resolves the conflict. Relaxing
immutability to permit silent deletion would remove the guarantee that makes
pinned versions trustworthy; leaving it absolute would mean the repository can
never remove published sensitive content.

## 4. Verification and Acceptance Criteria

- [x] `git grep` for the withdrawn hostnames, service names and ports returns
      nothing in the working tree. Verified with a case-insensitive scan for the
      hostnames, the four service names and the four ports.
- [x] `devops-manager` exposes exactly one version, `1.1.0`, with `latest` and
      `default` pointing at it.
- [x] The root payload matches `v1.1.0` exactly, scripts still executable. The
      validator's own root/current comparison covers this.
- [x] `task check` passes: 21 packages, 21 exact releases, immutability clean
      against `origin/main`.
- [x] `task test` passes: 18 tests, including five new cases covering the
      withdrawal ledger.

## 6. Outcome

`devops-manager` now publishes `1.1.0` only. `1.0.0` is withdrawn and recorded in
`WITHDRAWN.yaml`. The registry gained a declared-withdrawal path, documented in
`VERSIONING.md` and covered by tests.

Left for the repository owner, both outside this change:

- The withdrawn content remains in Git history and in any existing clone or fork.
  Removing it there needs a history rewrite and a force-push, which rewrites every
  published commit hash.
- The hostnames, ports and service names should be treated as disclosed. Whether
  that warrants any change to the host is an operational decision, not a
  repository one.

## 5. Risks and Mitigations

- *Risk*: Consumers pinned to `devops-manager` `1.0.0` break, because the version
  no longer resolves.
  *Mitigation*: Only version of a skill with no known external consumers; the
  alternative is leaving the disclosure published. Recorded here so the break is
  deliberate and visible.
- *Risk*: Redacting the tree is mistaken for removing the data.
  *Mitigation*: The non-goals state plainly that history still carries it, and the
  handover calls out history rewrite and the operational response as the
  owner's decisions.
