# Docker Monitoring and Logging with Prometheus, Grafana, and ELK Stack

## Project Overview
This project demonstrates how to set up monitoring and logging for Docker containers using Prometheus, Grafana, and the ELK stack (Elasticsearch, Logstash, Kibana).

## Tech Stack
- **Prometheus** (Monitoring)
- **Grafana** (Visualization)
- **ELK Stack** (Logging: Elasticsearch, Logstash, Kibana)
- **Docker Compose** (Container orchestration)

---

## Prerequisite

###🔹 Install the Latest Docker Compose

#### For Linux:
``` sh
sudo curl -SL https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose

```
#### Then, give execution permissions:


``` sh
sudo chmod +x /usr/local/bin/docker-compose
```

#### Verify installation:

``` sh
docker-compose --version
```
##### It should now show the latest version (e.g., v2.x.x).



## Implementation Steps

### Step 1: Set Up a Sample Web Application
We will create a simple Flask application that logs messages.

#### 1.1 Create `app.py`
```python
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

```

#### 1.2 Create `requirements.txt`
```txt
Flask
```

#### 1.3 Create `Dockerfile`
```dockerfile
# Use a minimal base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only requirements file to leverage caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user for security
RUN useradd -m appuser

# Copy application code
COPY . .

# Create the logs directory and set proper permissions
RUN mkdir -p /app/logs && chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Expose the application port
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
```

### Build the Flask Application Image

```sh
docker build -t flask_app .
```

### Run Flask Application

```sh
docker run --name flask_app -p 5000:5000 flask_app
```
---

### Step 2: Set Up `docker-compose.yml` with Prometheus, Grafana, and ELK Stack

#### Manually Pull Images (optional)

```sh
docker pull grafana/grafana:latest
docker pull logstash:7.10.1
docker pull kibana:7.10.1
docker pull elasticsearch:7.10.1
docker pull prom/prometheus:latest
```

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./app.log:/var/log/app.log

  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"

  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.10.1
    environment:
      - discovery.type=single-node
    ports:
      - "9200:9200"

  logstash:
    image: docker.elastic.co/logstash/logstash:7.10.1
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    depends_on:
      - elasticsearch

  kibana:
    image: docker.elastic.co/kibana/kibana:7.10.1
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch
```

---

### Step 3: Configure Prometheus for Monitoring
Create a `prometheus.yml` file:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'docker-metrics'
    static_configs:
      - targets: ['web:5000']
```

---

### Step 4: Configure Logstash for Logging
Create a `logstash.conf` file:

```plaintext
input {
  file {
    path => "/var/log/app.log"
    start_position => "beginning"
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "docker-logs"
  }
}
```

---

### Step 5: Run the Services
Execute the following command to start all the services:
```sh
docker-compose up --build
```

---

### Step 6: Access the Monitoring & Logging Dashboards

| Service      | URL                   |
|-------------|----------------------|
| Flask App   | http://localhost:5000 |
| Prometheus  | http://localhost:9090 |
| Grafana     | http://localhost:3000 |
| Kibana      | http://localhost:5601 |

---

### Step 7: Visualize Logs & Metrics

#### 7.1 Configure Grafana:
- Open Grafana at `http://localhost:3000`.
- Add Prometheus as a data source.
- Create dashboards for container metrics.
- Grafana's default credentials are:
   ` Username: admin`
   ` Password: admin`

#### 7.2 View Logs in Kibana:
- Open Kibana at `http://localhost:5601`. or `http://192.168.120.128:5601/app/home` or `http://192.168.120.128:5601/app/management/kibana/spaces`
- View logs stored in Elasticsearch.
- Create visualizations for container logs.

---

## Final Outcome ✅
- **Real-time monitoring** of container metrics with Prometheus & Grafana.
- **Centralized logging** using the ELK stack (Elasticsearch, Logstash, Kibana).
- **Hands-on experience** with observability tools in Docker environments.

🚀 Happy Monitoring & Logging! 🚀

