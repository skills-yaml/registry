#!/bin/bash
echo "### Docker Containers ###"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo ""
echo "### Systemd Services ###"
for svc in nginx docker; do
    STATUS=$(systemctl is-active $svc)
    echo "$svc: $STATUS"
done
echo ""
echo "### Resource Usage ###"
df -h / | awk 'NR==2 {print "Disk: " $5 " used (" $3 "/" $2 ")"}'
free -h | awk 'NR==2 {print "Memory: " $3 "/" $2}'
uptime | awk -F'load average:' '{print "Load:" $2}'
