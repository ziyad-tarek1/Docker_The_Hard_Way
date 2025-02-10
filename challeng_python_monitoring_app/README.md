
# Challenge try do it yourself! 🚀🔥
## Python Monitoring App (Dockerized)

This is a **Linux Host Monitoring** application that provides **real-time monitoring** of CPU, Memory, and Disk Usage.
It runs as a **Flask API** and **Dash web application** inside a **Docker container**.

## 🛠️ Features
- 📊 **Web-based Dashboard** for real-time monitoring.
- 🔍 **Flask API** for fetching utilization data (`/metrics`).
- 🐳 **Dockerized** for easy deployment.
- 🚀 **Runs on Host Machine** (using `--pid=host` and `/proc` mount).

---

## 🚀 How to Run

### 1️⃣ **Build the Docker Image**
```sh
docker build -t python-monitoring-app .
```

### 2️⃣ **Run the Container**
```sh
docker run -d \
  --pid=host \
  --privileged \
  -v /proc:/host_proc:ro \
  -v $(pwd)/logs:/app/logs \
  -p 5000:5000 \
  python-monitoring-app
```

---

## 📌 Endpoints

### **1. Metrics API**
Get **CPU, Memory, and Disk Usage** in JSON format:
```sh
curl http://localhost:5000/metrics
```

#### 📌 **Example Response:**
```json
{
  "cpu_usage": 27.5,
  "memory_usage": 45.3,
  "disk_usage": 58.1
}
```

### **2. Web UI**
- Open a browser and visit:  
  📌 **http://localhost:5000/**

---

## 📜 Logs
Logs are stored inside the `logs/` folder.

## 🛑 Stop the Container
```sh
docker stop $(docker ps -q --filter "ancestor=python-monitoring-app")
```

---

## 📷 Preview
| **Feature** | **Screenshot** |
|-------------|--------------|
| **Metrics API** | ![API Output](static/api-screenshot.png) |
| **Web UI** | ![Dashboard](static/ui-screenshot.png) |

---

## 📌 Notes
- This app **requires Docker with host access** to read system metrics.
- Tested on **Fedora**, **Ubuntu**, and **Debian**.
```

---

## **💡 Final Steps**
1. **Build the image**:
   ```sh
   docker build -t python-monitoring-app .
   ```

2. **Run the container**:
   ```sh
   docker run -d \
     --pid=host \
     --privileged \
     -v /proc:/host_proc:ro \
     -v $(pwd)/logs:/app/logs \
     -p 5000:5000 \
     python-monitoring-app
   ```

3. **Check logs**:
   ```sh
   docker logs -f $(docker ps -q --filter "ancestor=python-monitoring-app")
   ```

4. **Access API**:
   ```sh
   curl http://localhost:5000/metrics
   ```

5. **Open the Dashboard**:  
   Visit **http://localhost:5000/** in your browser.

---

## **🎯 Summary**
✅ **Monitors Linux Host CPU, RAM, and Disk**  
✅ **Provides JSON API (`/metrics`)**  
✅ **Web UI Dashboard for Real-time Charts**  
✅ **Dockerized for Easy Deployment**  

### 💡 Contributors
    - Ziyad Tarek Saeed - Author and Maintainer.

Happy coding! 🚀
