---
name: gcp-debug
description: Debug GCP services using logs and interrogate status of Cloud Run, Cloud Functions, GKE, and Compute Engine.
metadata:
  skm-version: "0.1.0"
---

# GCP Debugging

Instructs on how to debug Google Cloud Platform (GCP) services using Cloud Logging queries and status interrogation commands across Cloud Run, GKE, Cloud Functions, Compute Engine, and IAM.

## When to use

Use this skill when:
- A GCP service (Cloud Run, Cloud Functions, GKE Pod, or Compute Engine Instance) is failing, returning 5xx errors, crashing on startup, or timing out.
- You need to query, filter, or stream GCP logs programmatically using `gcloud logging`.
- You want to interrogate the configuration, status, and state of a GCP resource to find misconfigurations.
- You are troubleshooting service-to-service IAM communication or permission errors.
- You need to perform a diagnostic checklist on a newly deployed application that isn't responding.

## Core Workflows

### 1. Interrogating Cloud Logging
Cloud Logging (formerly Stackdriver) is the source of truth for errors and events.
- **Log Fetching**: Always target the specific resource type (`cloud_run_revision`, `gce_instance`, `k8s_container`, `cloud_function`).
- **Severity Filtering**: Use `severity>=ERROR` or `severity>=WARNING` to skip verbose operational noise.
- **Payload Search**: Filter using `textPayload` or structured `jsonPayload` fields.

```bash
gcloud logging read 'resource.type="cloud_run_revision" AND severity>=ERROR' --limit=50 --format=json
```

### 2. Interrogating Service Status
Before examining code, inspect the control plane status of the target compute service.
- **Cloud Run**: Check revision health status, latest actions, and traffic splitting.
- **Cloud Functions**: Validate build/deployment state, active triggers, and network ingress settings.
- **GKE**: Inspect deployment status, pod lifecycle states (e.g., `CrashLoopBackOff`), and Kubernetes service endpoints.
- **Compute Engine (GCE)**: Check the VM instance status (`running`, `terminated`), serial port logs, and startup script execution results.

```bash
# Example Cloud Run interrogation
gcloud run services describe <service-name> --region=<region> --format=json
```

### 3. Diagnosing IAM and Connectivity Issues
If logs show permission errors, investigate the active service account and its bindings:
- Determine the identity running the resource (e.g., the service account attached to Cloud Run).
- Query Policy Analyzer or test policy IAM bindings to verify permissions.
- Validate VPC connector settings or internal firewall rules if timeouts occur.

## References

- **gcloud CLI Cheat Sheet**: For complex query filters, JSON formatting flags, and service-specific diagnostic commands, see [references/gcloud-cheatsheet.md](references/gcloud-cheatsheet.md).
