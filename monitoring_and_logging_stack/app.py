import os
import logging
from flask import Flask

app = Flask(__name__)

# Ensure log directory exists
log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)

# Configure logging
log_file = os.path.join(log_dir, "app.log")
logging.basicConfig(filename=log_file, level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home route accessed")
    return "Monitoring Docker App"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
