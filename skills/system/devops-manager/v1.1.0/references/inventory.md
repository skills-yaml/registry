# Service Inventory

A service inventory tells you what *should* be running, so `scripts/health.sh`
output means something. This skill does not ship one: the inventory describes a
particular machine, and it belongs with that machine rather than in a shared
registry.

## Build the inventory from the host

Run these on the machine and record what they report:

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
systemctl list-units --type=service --state=running
ss -tulpn | grep LISTEN
```

## Keep it out of version control

An inventory names internal services, ports and hostnames. Together they map the
host's attack surface, so keep it where the host is administered, not in a public
repository:

- Write it to a path the agent can read at runtime, such as
  `/etc/devops-manager/inventory.md` or a file in the operator's home directory.
- If it has to live in a repository, keep that repository private and confirm the
  visibility before the first commit.
- Never record credentials, tokens or connection strings in it, whatever the
  repository's visibility.

## Suggested shape

| Service | Type | Port | Description |
|---------|------|------|-------------|
| `<name>` | Docker or Systemd | `<port>` | `<what it serves>` |

Record expected public hostnames the same way, alongside the service each one
routes to.
