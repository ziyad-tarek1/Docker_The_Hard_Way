# **Flask Application - Docker Setup**

This repository contains a simple Flask application that runs inside a Docker container. The project follows best practices for containerization and deployment.

## **Table of Contents**
- [Requirements](#requirements)  
- [Project Structure](#project-structure)  
- [Building and Running the Image](#building-and-running-the-image)  
- [Testing the Application](#testing-the-application)  
- [Pushing the Image to Docker Hub](#pushing-the-image-to-docker-hub)  
- [Dockerfile Explanation](#dockerfile-explanation)  
- [License](#license)  

---

## **Requirements**
Ensure you have the following installed before running the application:
- **Docker** (latest version recommended)  

---

## **Project Structure**
```
basic-flask-app/
│── static/                   # Static files (CSS, images)
│── templates/                # HTML templates for Flask
│── routes.py                 # Flask application routes
│── requirements.txt          # Python dependencies
│── Dockerfile                # Docker build instructions
│── LICENSE                   # Project license
│── README.md                 # Documentation
```

---

## **Building and Running the Image**
### **1. Build the Docker Image**
Run the following command to build the Docker image with the name `ITI-flask-lab2`:
```sh
docker build -t ITI-flask-lab2 .
```

### **2. Run the Container with Memory Limit (100MB)**
Start the container and bind **port 5000 inside the container to port 80 on the host**:
```sh
docker run -d --memory=100m -p 127.0.0.1:80:5000 --name flask-container ITI-flask-lab2
```

---

## **Testing the Application**
### **Check if the container is running**
```sh
docker ps
```

### **Access the application in your browser**
Open:
```
http://127.0.0.1
```

or use **curl** to test:
```sh
curl http://127.0.0.1
```

---

## **Pushing the Image to Docker Hub**
### **1. Log in to Docker Hub**
```sh
docker login -u ziyadtarek99
```

### **2. Tag the Image**
```sh
docker tag ITI-flask-lab2 ziyadtarek99/iti-flask-lab2:latest
```

### **3. Push the Image**
```sh
docker push ziyadtarek99/iti-flask-lab2:latest
```

---

## **Dockerfile Explanation**
This Dockerfile builds a lightweight Flask application container.

```dockerfile
# Use the official Python image from Docker Hub
FROM python:3.9-slim AS base

# Set environment variables to optimize Python behavior
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "routes.py"]  # Change to app.py if necessary
```


