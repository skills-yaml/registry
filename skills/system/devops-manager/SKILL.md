---
name: devops-manager
description: Manage system services, check health, security, and updates on this Debian/Docker machine. Use when the user needs to inspect Docker containers, system logs, update software, or check the status of core services like Nginx or PostgreSQL.
---

# DevOps Manager

This skill helps you manage and monitor the services running on this system.

## Core Workflows

### Health Monitoring
To check the overall health of the system and its services:
1. Run the health script: `bash scripts/health.sh`
2. Inspect the output for stopped containers or inactive systemd services.
3. Check disk and memory usage to ensure the system isn't under pressure.

### Hostname and identity alignment
Use this when the user wants the VM name, local hostname, or Tailscale-facing name to line up.
1. Set the system hostname with `hostnamectl set-hostname <new-name>`.
2. Update `/etc/hostname` to the same short name.
3. Preserve provider-managed `/etc/hosts` entries and add the new alias to the existing host line instead of replacing it.
4. Verify with `hostnamectl --static`, `cat /etc/hostname`, and `grep -n '<ip>' /etc/hosts`.
5. If the user wants the MagicDNS node name changed too, use Tailscale's hostname setting separately; Linux hostname changes alone do not guarantee a new Tailscale node name.

See [references/hostname-and-tailscale-naming.md](references/hostname-and-tailscale-naming.md) for the concise recipe and pitfall notes.

### Managing Updates
To check for and apply updates:
1. Run the updates script: `bash scripts/updates.sh`
2. If system updates are available, run `sudo apt update && sudo apt upgrade -y`.
3. If newer Docker images are available, pull them with `docker pull <image_name>` and restart the service (e.g., `docker compose up -d` in the relevant directory).

### Security Auditing
To perform a quick security check:
1. Run the security script: `bash scripts/security.sh`
2. Review listening ports to ensure only expected services are exposed.
3. Check for failed login attempts to identify potential brute-force attacks.

## Reference Materials

- **Service Inventory**: See [inventory.md](references/inventory.md) for a list of expected services and their ports.

## Troubleshooting

- **Container Down**: If a container is stopped, check its logs: `docker logs <container_id>`.
- **Nginx Error**: If Nginx is down, check configuration with `nginx -t` and logs with `journalctl -u nginx`.
