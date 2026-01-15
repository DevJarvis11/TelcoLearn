# Capstone Kubernetes Monitoring & Alerting Project

## Kubernetes Pod State Monitoring with External Grafana Log Visualization

--- 

## 1. Project Overview

This capstone project implements a Kubernetes-native monitoring and alerting system that continuously observes application pod states, detects runtime changes, sends real-time alerts via Telegram, and provides both custom dashboards and Grafana-based log visualization.

The design follows industry best practices:
- Lightweight
- Non-intrusive
- Secure
- Extensible

Grafana integration is implemented as an add-on observability layer, ensuring zero impact on the core project logic.

---

## 2. Problem Statement

Modern Kubernetes environments operate over highly dynamic virtual networks where pods are ephemeral, IP addresses change frequently, and service connectivity is abstracted through orchestration layers. Failures such as pod restarts, rescheduling, or crashes can silently disrupt internal service communication.

Traditional monitoring stacks may introduce unnecessary complexity for lightweight or internal systems. There is a need for a network-aware, Kubernetes-native monitoring solution that can detect pod-level changes, provide real-time visibility, and alert engineers without relying on heavyweight observability frameworks.

---

## 3. Key Features

- Continuous Kubernetes pod state monitoring
- Detection of pod creation, deletion, and replacement
- STABLE / UNSTABLE state tracking
- Real-time Telegram alerts
- REST APIs for logs and status
- Web-based dashboard (Flask)
- External Grafana integration for live logs
- Zero modification to existing code

---

## 4. Architecture Overview

Application Pods → Kubernetes API → Monitor Service → Dashboard / Telegram  
Logs → Promtail (stdin) → Loki → Grafana

---

## 5. Folder Structure

capstone-monitoring/
├── app.py
├── dashboard.py
├── monitor.py
├── Dockerfile
├── requirements.txt
├── cluster_network_observer.sh
├── templates/
│   └── index.html
├── k8s/
│   ├── app-deployment.yaml
│   ├── app-service.yaml
│   ├── dashboard-deployment.yaml
│   ├── dashboard-service.yaml
│   ├── monitor-deployment.yaml
│   ├── monitor-rbac.yaml
│   └── telegram-secret.yaml
└── README.md

---

## 6. Kubernetes Deployment Commands

kubectl apply -f k8s/telegram-secret.yaml
kubectl apply -f k8s/app-deployment.yaml
kubectl apply -f k8s/app-service.yaml
kubectl apply -f k8s/dashboard-deployment.yaml
kubectl apply -f k8s/dashboard-service.yaml
kubectl apply -f k8s/monitor-rbac.yaml
kubectl apply -f k8s/monitor-deployment.yaml

---

## 7. Access Dashboard

kubectl port-forward svc/dashboard 9090:8080
http://localhost:9090

---

## 8. Monitor Logs

kubectl logs -f -l app=monitor

---

## 9. Grafana Integration (No YAML)

Run Loki:
docker run -d --name loki -p 3100:3100 grafana/loki:2.9.3

Run Grafana:
docker run -d --name grafana -p 3000:3000 grafana/grafana:10.2.2

Stream logs:
kubectl logs -f -l app=monitor | docker run -i grafana/promtail:2.9.3 -stdin -client.url=http://host.docker.internal:3100/loki/api/v1/push

Grafana URL: http://localhost:3000  
Credentials: admin / admin

---

## 10. Grafana Queries

Equivalent to kubectl logs:
{job="stdin"}

CRITICAL logs:
{job="stdin"} |= "CRITICAL"

RECOVERY logs:
{job="stdin"} |= "RECOVERY"

---

## 11. Conclusion

This project demonstrates Kubernetes-native monitoring, networking awareness, alerting, and observability with a non-intrusive Grafana integration suitable for real-world engineering environments.
