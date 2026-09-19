# Hostname and Tailscale naming

Use this when the user wants the VM name to match the service or Tailscale identity.

## What to change
- `hostnamectl set-hostname <new-name>` updates the system hostname.
- `/etc/hostname` should contain the same short hostname.
- `/etc/hosts` should keep provider-added internal entries and add the new short name as an alias, not delete the existing cloud metadata hostname.

## Verification
- `hostnamectl --static`
- `cat /etc/hostname`
- `grep -n '<ip>' /etc/hosts`

## Tailscale note
- Changing the Linux hostname does not necessarily rename the Tailscale node.
- If the goal is a new MagicDNS node name, also use Tailscale's hostname setting for the device.
- If the goal is just local consistency, aligning the Linux hostname and local hosts file is enough.

## Pitfall
- Do not overwrite cloud-generated `/etc/hosts` entries; preserve them and append the new alias to the existing line when possible.
