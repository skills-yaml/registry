# GCP Debugging and gcloud Diagnostics Cheat Sheet

This reference document contains common, high-impact `gcloud` recipes and diagnostic commands categorized by resource type.

---

## 1. Cloud Logging (gcloud logging)

### Querying with Log Filters
Always prefer highly specific filters to avoid fetching millions of lines.

```bash
# Query logs for a specific Cloud Run service with severe/error status
gcloud logging read 'resource.type="cloud_run_revision" AND resource.labels.service_name="<service-name>" AND severity>=ERROR' --limit=30 --format="table(timestamp, severity, textPayload)"

# Search inside jsonPayload or textPayload for generic error text
gcloud logging read 'textPayload:"failed" OR jsonPayload.message:"exception"' --limit=20

# Stream logs in real-time (like tail -f)
gcloud logging tail 'resource.type="cloud_run_revision" AND resource.labels.service_name="<service-name>"'
```

### Resource Types Reference
- Cloud Run: `cloud_run_revision`
- Cloud Functions (Gen 2): `cloud_run_revision` (built on Cloud Run)
- Cloud Functions (Gen 1): `cloud_function`
- Kubernetes (GKE) Container: `k8s_container`
- Compute Engine (VM): `gce_instance`
- HTTP(S) Load Balancer: `http_load_balancer`

---

## 2. Cloud Run Diagnostics

### Inspecting Revision Status and Routing
```bash
# Is the service up? Get active URL, ingress, memory limits, and traffic distribution
gcloud run services describe <service-name> --region=<region> --format="yaml(status,spec)"

# List revisions to see if a newly deployed revision is crashing (has 0% traffic)
gcloud run revisions list --service=<service-name> --region=<region> --limit=5

# Describe reasons behind a failing revision
gcloud run revisions describe <revision-name> --region=<region> --format="yaml(status.conditions)"
```

### Common Cloud Run Pitfalls
- **Port Invariant**: Cloud Run requires the app to listen on the port specified by the `$PORT` environment variable (default: `8080`). If the app listens on a hardcoded port like `5000` or fails to bind on `0.0.0.0`, the revision container status turns to `CrashLoopBackOff` or fails its startup probe.
- **Memory Limits**: Heavy workloads (e.g. ML inference, large PDF processing) abort silently when exceeding memory limits. Check logs for `Container sandbox limit exceeded` or `Memory limit exceeded`.

---

## 3. GKE (Google Kubernetes Engine) Diagnostics

### Control Plane and Node Status
```bash
# Get cluster summary and endpoint security state
gcloud container clusters describe <cluster-name> --zone=<zone> --format="yaml(status, endpoint, nodePools)"

# Fetch credentials to use with native kubectl
gcloud container clusters get-credentials <cluster-name> --zone=<zone>
```

### Kubectl Diagnostics
Once credentials are set, evaluate Kubernetes workloads directly:
```bash
# Check Pod states (look for CrashLoopBackOff, ImagePullBackOff, Pending)
kubectl get pods -n <namespace> -o wide

# Describe a failing pod to inspect life cycle events (e.g. out of memory OOMKilled, missing secrets, failing probes)
kubectl describe pod <pod-name> -n <namespace>

# Review container standard logs
kubectl logs <pod-name> -n <namespace> --tail=100
# If the pod crashed, view previous instance logs
kubectl logs <pod-name> -n <namespace> --previous
```

---

## 4. Cloud Functions (Gen 2) Diagnostics

Since Gen 2 functions run on Cloud Run, use the Run commands above, or:
```bash
# Check function deployment status
gcloud functions describe <function-name> --region=<region> --gen2 --format="yaml(status, state)"

# Read build-time failures (e.g. failing pip install, npm compile error)
# Cloud Functions uses Cloud Build under the hood
gcloud builds list --limit=5
gcloud builds log <latest-build-id>
```

---

## 5. Compute Engine (GCE) Diagnostics

### Instance State and Metadata
```bash
# Get GCE instance status, network tags, and internal/external IPs
gcloud compute instances describe <instance-name> --zone=<zone> --format="yaml(status, networkInterfaces, tags)"

# Get startup script or shutdown script logs from the serial console output
gcloud compute instances get-serial-port-output <instance-name> --zone=<zone> --port=1
```

### Common VM Failures
- **Startup Script Failures**: Watch serial port output 1 closely for installation fails or script crashes.
- **Firewall Isolation**: If the instance is running but unresponsive, verify the VPC firewall rules allow inbound traffic on required ports:
  ```bash
  gcloud compute firewall-rules list --filter="network=<network-name> AND allowed.ports:<target-port>"
  ```

---

## 6. IAM and Permissions Interrogation

If requests fail with `403 Forbidden` or `Permission Denied`:

1. **Find Attached Service Account**:
   - For Cloud Run: `gcloud run services describe <service-name> --region=<region> --format="value(spec.template.spec.serviceAccountName)"`
   - For GCE: `gcloud compute instances describe <instance-name> --zone=<zone> --format="value(serviceAccounts.email)"`

2. **Retrieve IAM Policies and Roles**:
   ```bash
   # Check if the service account has the necessary role on the project
   gcloud projects get-iam-policy <project-id> --filter="bindings.members:<service-account-email>" --format="yaml(bindings)"
   ```

3. **Check Impersonation Capabilities**:
   Ensure your local credentials or the executor credentials can act as the target service account.
