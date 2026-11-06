# Investigate Applicable Attack Paths

Select the boundaries actually present in the requested scope. These questions
guide source tracing, not automatic findings. Apply the skill's evidence gate and
execution limits to every lead, and stop when the assigned invariant is settled.
Report newly discovered scope separately rather than silently widening the hunt.

## Authority and Business Workflows

Trace caller identity and trusted tenant/owner context to the final resource
operation. Compare single-item, batch, export, import, background-job and recovery
paths. Authentication, a valid object ID or a tenant field does not establish
authorization. Check permissions on every item and whether body fields can
override trusted scope. Use the skill's domain-model route for schema changes.

For stateful operations, inspect skipped/repeated steps, replay, revocation,
expiration, concurrent check/use, partial failure, retry and rollback. Check
numeric bounds, units, precision and negative/zero values only where accepted.
Identify the actual protected resource or authority lost before reporting impact.

## Input, Files and Network Destinations

Follow untrusted values, keys and metadata through parsing, storage and later use
in queries, commands, templates, paths, logs, callbacks or policies. Compare the
exact guarantees each producer supplies with the next consumer's assumptions.
Escaping for one context does not establish safety in another.

For files and archives, inspect canonicalization, symlink and hard-link behavior,
extraction destinations and races between validation and use. For URL fetches,
compare URL parsers, redirects, resolved addresses and final destination checks.
Do not probe a live network or read host secrets to establish a suspected flaw.

## HTTP, Browser and Identity Protocols

Where a request crosses proxies, caches or protocol translations, compare framing,
normalization, duplicate fields and cache keys at each hop. Trace which parser
and deployment mode are actually active. Unknown proxy/provider behavior is an
exact validation blocker, not an assumed bypass.

For sessions, tokens, OAuth/OIDC and recovery/linking flows, examine issuer,
audience, signature, redirect binding, state/nonce, expiration, replay and resource
scope where applicable. Inspect browser origin/message checks, CSRF boundaries,
output rendering and service-worker/cache scope. A missing cookie flag or broad
header is a lead; establish the sensitive operation and reachable effect.

## Cryptography, Secrets and Release Authority

Trace security-critical randomness, key selection, authenticated encryption,
signature verification and failure fallbacks. Examine what a token is bound to,
where secrets can be logged/rendered, and whether revocation reaches cached or
delegated credentials. Never include the secret value in evidence.

For dependencies, CI, plugins, signing and updates, follow untrusted source,
artifact or metadata to the execution/release identity. Check integrity, pinned
resolution, trusted event context, artifact provenance and promotion consistency.
Read build hooks before execution. Do not publish, change credentials or invoke
cloud writes as a test; retain the existing infrastructure/approval boundaries.

## Data Copies, Resources and Native Code

Trace ownership through caches, indexes, exports, notifications, backups,
deletion and restore. Check all readers/writers and alternate selectors. A
correct primary query does not establish isolation of its derived copies.

For availability, identify whose shared CPU, memory, disk, workers, connections
or paid quota can be consumed, then inspect quotas, cancellation, backpressure
and recovery. Distinguish accepted ordinary work and self-impact from loss of
a shared protected resource. Never stress a live or shared process.

For native/FFI, parser or concurrency boundaries, trace lengths, integer/ABI
conversions, allocation lifetimes, ownership and synchronization to the exact
unsafe operation. Use a bounded sanitizer/fixture result only within the required
sandbox. A malformed input or generic crash does not prove arbitrary execution.
