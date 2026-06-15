# Service Inventory

| Service | Type | Port | Description |
|---------|------|------|-------------|
| OpenClaw Gateway | Docker | 18789 | AI agent gateway |
| Paperclip App | Docker | 6969 (internal) / 6970 (host) | Agent orchestration platform |
| Paperclip DB | Docker | 5432 | PostgreSQL database |
| Open WebUI | Docker | 8081 | Local LLM interface (stopped) |
| Nginx | Systemd | 80, 443 | Reverse proxy for `a.delfii.io` and `cmd.delfii.io` |
| Docker | Systemd | N/A | Container runtime |

## Expected Domains
- `a.delfii.io`: Points to OpenClaw Gateway.
- `cmd.delfii.io`: Points to Paperclip App.
