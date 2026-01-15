#!/bin/bash

PCAP_FILE="dashboard_portforward_traffic.pcap"
PORT=9090
INTERFACE="any"

echo "=========================================="
echo " K8s PORT-FORWARD NETWORK OBSERVER"
echo "=========================================="

# Root check
if [[ $EUID -ne 0 ]]; then
  echo "[ERROR] Run as root:"
  echo "sudo $0"
  exit 1
fi

echo
echo "[1] PORT-FORWARD STATUS"
echo "Ensure this is running in another terminal:"
echo "kubectl port-forward svc/dashboard 9090:8080"

echo
echo "[2] LISTENING PORT CHECK"
ss -lnt | grep ":$PORT" || {
  echo "[ERROR] Port $PORT not listening"
  exit 1
}

echo
echo "[3] STARTING PACKET CAPTURE"
echo "Interface : $INTERFACE"
echo "Port      : $PORT"
echo "Output    : $PCAP_FILE"
echo
echo "👉 Open http://localhost:$PORT"
echo "👉 Refresh multiple times"
echo "👉 Press Ctrl+C after 10–15 seconds"

tcpdump -i $INTERFACE tcp port $PORT -w $PCAP_FILE

echo
echo "[4] CAPTURE COMPLETE"
ls -lh $PCAP_FILE

echo
echo "=========================================="
echo " DONE"
echo "=========================================="
