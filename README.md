# Docker and Kubernetes Projects Repository

This repository contains a collection of Docker and Kubernetes projects, ranging from simple containerized applications to advanced multi-container setups and Kubernetes deployments. Each project is designed to help you understand and practice different aspects of containerization, orchestration, and DevOps workflows.

---

## Table of Contents

1. [Projects Overview](#projects-overview)
2. [Getting Started](#getting-started)
3. [Project Details](#project-details)
   - [Analog Clock](#analog-clock)
   - [Dinosaur Game](#dinosaur-game)
   - [Nana Website](#nana-website)
   - [Python Todo App](#python-todo-app)
   - [React App](#react-app)
   - [Simple Flask Web Application](#simple-flask-web-application)
   - [Webserver Load Balancer](#webserver-load-balancer)
   - [Tetris Game](#tetris-game)
   - [Multi-Container App](#multi-container-app)
   - [Monitoring and Logging Stack](#monitoring-and-logging-stack)
   - [Voting App](#voting-app)
   - [Kubernetes Voting App](#kubernetes-voting-app)
   - [Kubernetes Advanced Voting App](#kubernetes-advanced-voting-app)
   - [challeng python monitoring app](#challeng_python_monitoring_app)
4. [Contributing](#contributing)
5. [License](#license)

---

## Projects Overview

This repository includes the following projects:

1. **Analog Clock**: A simple web-based analog clock application.
2. **Dinosaur Game**: A clone of the Chrome Dino game, containerized with Docker.
3. **Nana Website**: A website project created with the help of Tech With Nana.
4. **Python Todo App**: A Python-based todo application that supports both Docker and Docker Compose.
5. **React App**: A basic React application with Docker setup.
6. **Simple Flask Web Application**: A minimal Flask web app with Docker and Docker Compose support.
7. **Webserver Load Balancer**: A Docker Compose project demonstrating load balancing with Nginx.
8. **Tetris Game**: A Tetris game built with React and containerized with Docker.
9. **Multi-Container App**: A Python app that works with both MySQL and PostgreSQL, using Docker Compose.
10. **Monitoring and Logging Stack**: A Docker Compose stack for monitoring and logging using Prometheus, Grafana, and ELK.
11. **Voting App**: A multi-container voting application with Docker Compose.
12. **Kubernetes Voting App**: A simple Kubernetes deployment of the voting app using pre-configured images.
13. **Kubernetes Advanced Voting App**: An advanced Kubernetes deployment where images are built from scratch.

---

## Getting Started

To get started with any of the projects:

1. Clone the repository:
   ```bash
   git clone https://github.com/ziyad-tarek1/Docker_The_Hard_Way.git
   cd Docker_The_Hard_Way
   ```

2. Navigate to the project folder:
   ```bash
   cd <project-folder>
   ```

3. Follow the instructions in the project's `README.md` or `docker-compose.yml` file to build and run the application.

---

## Project Details

### Analog Clock
- **Description**: A web-based analog clock built with HTML, CSS, and JavaScript.
- **Files**:
  - `Dockerfile`
  - `index.html`
  - `script.js`
  - `styles.css`
- **How to Run**:
  ```bash
  docker build -t analog-clock .
  docker run -p 80:80 analog-clock
  ```

### Dinosaur Game
- **Description**: A clone of the Chrome Dino game, containerized with Docker and Nginx.
- **Files**:
  - `Dockerfile`
  - `index.html`, `index.css`, `index.js`
  - `nginx.conf`
- **How to Run**:
  ```bash
  docker build -t dino-game .
  docker run -p 80:80 dino-game
  ```

### Nana Website
- **Description**: A website project created with the help of Tech With Nana.
- **Files**:
  - `Dockerfile`
  - `index.html`
  - `server.js`
- **How to Run**:
  ```bash
  docker build -t nana-website .
  docker run -p 3000:3000 nana-website
  ```

### Python Todo App
- **Description**: A Python-based todo app that supports Docker and Docker Compose.
- **Files**:
  - `Dockerfile`
  - `docker-compose.yml`
  - `app.py`
  - `requirements.txt`
- **How to Run**:
  ```bash
  docker-compose up
  ```

### React App
- **Description**: A basic React application with Docker setup.
- **Files**:
  - `Dockerfile`
  - `package.json`
  - `src/`, `public/`
- **How to Run**:
  ```bash
  docker build -t react-app .
  docker run -p 3000:3000 react-app
  ```

### Simple Flask Web Application
- **Description**: A minimal Flask web app with Docker and Docker Compose support.
- **Files**:
  - `Dockerfile`
  - `docker-compose.yml`
  - `app.py`
- **How to Run**:
  ```bash
  docker-compose up
  ```

### Webserver Load Balancer
- **Description**: A Docker Compose project demonstrating load balancing with Nginx.
- **Files**:
  - `docker-compose.yml`
  - `nginx.conf`
  - `web1/`, `web2/`, `web3/`
- **How to Run**:
  ```bash
  docker-compose up
  ```

### Tetris Game
- **Description**: A Tetris game built with React and containerized with Docker.
- **Files**:
  - `Dockerfile`
  - `package.json`
  - `src/`, `public/`
- **How to Run**:
  ```bash
  docker build -t tetris-game .
  docker run -p 3000:3000 tetris-game
  ```

### Multi-Container App
- **Description**: A Python app that works with both MySQL and PostgreSQL, using Docker Compose.
- **Files**:
  - `Dockerfile`
  - `docker-compose.yml`
  - `app.py`
- **How to Run**:
  ```bash
  docker-compose up
  ```

### Monitoring and Logging Stack
- **Description**: A Docker Compose stack for monitoring and logging using Prometheus, Grafana, and ELK.
- **Files**:
  - `docker-compose.yml`
  - `prometheus.yml`
  - `logstash.conf`
- **How to Run**:
  ```bash
  docker-compose up
  ```

### Voting App
- **Description**: A multi-container voting application with Docker Compose.
- **Files**:
  - `docker-compose.yml`
  - `vote/`, `result/`, `worker/`
- **How to Run**:
  ```bash
  docker-compose up
  ```

### Kubernetes Voting App
- **Description**: A simple Kubernetes deployment of the voting app using pre-configured images.
- **Files**:
  - Kubernetes manifests (`postgres-deploy.yaml`, `redis-deploy.yaml`, etc.)
- **How to Run**:
  ```bash
  kubectl apply -f <manifest-file>
  ```

### Kubernetes Advanced Voting App
- **Description**: An advanced Kubernetes deployment where images are built from scratch.
- **Files**:
  - Kubernetes manifests (`k8s/`)
  - Dockerfiles (`container/`)
- **How to Run**:
  ```bash
  kubectl apply -f <manifest-file>
  ```
### challeng_python_monitoring_app
- **Description**: An advanced docker project try containerized it yourself.


---

### 👨‍💻 License
This project is licensed under a custom license. Unauthorized use, distribution, or modification is prohibited. Refer to the LICENSE file for details.

---

### 💡 Contributors
    - Ziyad Tarek Saeed - Author and Maintainer.

Happy coding! 🚀
