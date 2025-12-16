#!/bin/bash

HOST="192.168.10.101"
PORT=22

check_port() {
    nc -z -w 2 $HOST $PORT
    if [ $? -eq 0 ]; then
        echo "Port $PORT on $HOST is OPEN"
    else
        echo "Port $PORT on $HOST is CLOSED"
    fi
}

while true; do
    check_port
    sleep 3
done
