import time
import os
import requests
from flask import Flask, jsonify
from kubernetes import client, config
from threading import Thread

LABEL_SELECTOR = "app=app"
CHECK_INTERVAL = 3

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

app = Flask(__name__)
logs = []
last_pods = None
state = "STABLE"


def log(msg):
    ts = time.strftime("%H:%M:%S")
    entry = f"[{ts}] {msg}"
    logs.append(entry)
    logs[:] = logs[-200:]
    print(entry, flush=True)


def send_telegram(msg):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": msg},
            timeout=5
        )
    except:
        log("[WARN] Telegram error ignored")


def monitor_loop():
    global last_pods, state

    config.load_incluster_config()
    v1 = client.CoreV1Api()

    log("Monitor started – pod state monitoring")

    while True:
        pods = v1.list_namespaced_pod(
            namespace="default",
            label_selector=LABEL_SELECTOR
        ).items

        pod_names = sorted(p.metadata.name for p in pods)
        log(f"[CHECK] pods={pod_names}")

        if last_pods is None:
            last_pods = pod_names
        elif pod_names != last_pods:
            log("[CRITICAL] Pod change detected")
            send_telegram(
                f"🚨 CRITICAL ALERT\nOld: {last_pods}\nNew: {pod_names}"
            )
            last_pods = pod_names
            state = "UNSTABLE"
        elif state == "UNSTABLE":
            log("[RECOVERY] Pods stable")
            send_telegram(
                f"✅ RECOVERY ALERT\nStable pods: {pod_names}"
            )
            state = "STABLE"

        time.sleep(CHECK_INTERVAL)


@app.route("/logs")
def get_logs():
    return jsonify(logs)


@app.route("/status")
def get_status():
    return jsonify({"state": state})


if __name__ == "__main__":
    Thread(target=monitor_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=9090)
