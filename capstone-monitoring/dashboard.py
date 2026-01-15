from flask import Flask, render_template, jsonify
import requests

MONITOR_URL = "http://monitor:9090"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/logs")
def logs():
    return jsonify(requests.get(f"{MONITOR_URL}/logs", timeout=2).json())

@app.route("/api/status")
def status():
    return jsonify(requests.get(f"{MONITOR_URL}/status", timeout=2).json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
