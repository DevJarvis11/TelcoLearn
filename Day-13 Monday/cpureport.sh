#!/bin/bash

# File to store CPU usage logs
LOGFILE="/tmp/cpu_usage_report.log"

echo "CPU Usage Report Started at $(date)" >> "$LOGFILE"

# Run for 10 minutes (10 iterations × 1 minute)
for i in {1..10}
do
    echo "---- Report #$i at $(date) ----" >> "$LOGFILE"
    
    # Capture CPU usage using top (non-interactive)
    top -bn1 | grep "Cpu(s)" >> "$LOGFILE"

    sleep 60     # wait 1 minute
done

echo "CPU Usage Report Completed at $(date)" >> "$LOGFILE"
