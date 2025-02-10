from flask import Flask, render_template, jsonify
import psutil
import os
import time

app = Flask(__name__)

LOG_DIR = "/app/logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "monitor.log")


def log_usage():
    """Logs system resource usage to a file."""
    with open(LOG_FILE, "a") as f:
        while True:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory().percent
            f.write(f"CPU: {cpu}%, Memory: {memory}%\n")
            time.sleep(3)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/metrics")
def metrics():
    """Fetches real-time system resource usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    processes = []
    for proc in psutil.process_iter(["pid", "name", "memory_percent", "cpu_percent", "num_threads"]):
        try:
            processes.append({
                "pid": proc.info["pid"],
                "name": proc.info["name"],
                "memory": round(proc.info["memory_percent"], 2),
                "cpu": round(proc.info["cpu_percent"], 2),
                "threads": proc.info["num_threads"]
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    processes = sorted(processes, key=lambda p: p["cpu"], reverse=True)[:10]

    return jsonify({"cpu": cpu_usage, "memory": memory_usage, "processes": processes})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
