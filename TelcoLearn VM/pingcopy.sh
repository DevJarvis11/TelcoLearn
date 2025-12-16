#!/bin/bash

websites=("google.com" "yahoo.com" "bing.com" "duckduckgo.com" "stackoverflow.com")

total_bytes=0
total_time=0
total_count=0

echo "Pinging websites..."

for site in "${websites[@]}"; do
    echo "--------------------------------"
    echo "Pinging $site (5 times):"

    ping_output=$(ping -c 5 "$site")
    
    while read -r line; do
        if [[ $line == *"bytes from"* ]]; then
            echo "$line"
            
            # Correct byte extraction
            bytes=$(echo "$line" | awk '{print $1}')
            
            # Time extraction
            time=$(echo "$line" | awk -F'time=' '{print $2}' | awk '{print $1}')
            
            # Accumulate totals
            total_bytes=$(echo "$total_bytes + $bytes" | bc)
            total_time=$(echo "$total_time + $time" | bc)
            total_count=$((total_count + 1))
        fi
    done <<< "$ping_output"
done

average_bytes=$(echo "scale=2; $total_bytes / $total_count" | bc)
average_time=$(echo "scale=2; $total_time / $total_count" | bc)

echo "--------------------------------"
echo "Average bytes across all pings: $average_bytes bytes"
echo "Average time across all pings: $average_time ms"
