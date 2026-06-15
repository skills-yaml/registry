#!/bin/bash
echo "### Listening Ports ###"
ss -tulpn | grep LISTEN | awk '{print $5, $7}' | sort -u

echo ""
echo "### Failed Login Attempts (Last 5) ###"
grep "Failed password" /var/log/auth.log 2>/dev/null | tail -n 5 || echo "No failed logs or access denied."

echo ""
echo "### Firewall Status ###"
if command -v ufw > /dev/null; then
    ufw status
elif command -v nft > /dev/null; then
    echo "nftables found. Listing ruleset summary..."
    nft list ruleset | head -n 10
elif command -v iptables > /dev/null; then
    echo "iptables found. Checking rules..."
    iptables -L -n | head -n 5
else
    echo "No common firewall tool (ufw, nft, iptables) found."
fi
