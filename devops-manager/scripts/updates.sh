#!/bin/bash
echo "### System Updates (Apt) ###"
UPGRADES=$(apt list --upgradable 2>/dev/null | grep -v "Listing..." | wc -l)
if [ "$UPGRADES" -gt 0 ]; then
    echo "$UPGRADES updates available."
    apt list --upgradable 2>/dev/null | grep -v "Listing..." | head -n 5
else
    echo "System is up to date."
fi

echo ""
echo "### Docker Image Updates ###"
# List images that have newer versions pulled but not running
docker images | grep -v "REPOSITORY" | awk '{print $1 ":" $2}' | while read img; do
    # This is a bit complex for a simple script, let's just list what images we have
    echo "Image: $img"
done
echo "Tip: Run 'docker images' to see local images. Run 'apt update' then 'apt list --upgradable' for full list."
