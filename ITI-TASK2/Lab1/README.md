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

![image](https://github.com/user-attachments/assets/42df3cb5-ed39-4490-ad2f-96fc1f5e6c9d)

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
Run the following command to build the Docker image with the name `iti-flask-lab2`:
```sh
docker build -t iti-flask-lab2 .
```
![image](https://github.com/user-attachments/assets/113b134d-b06e-48fa-841e-9f91afc05285)

### **2. Run the Container with Memory Limit (100MB)**
Start the container and bind **port 5000 inside the container to port 80 on the host**:
```sh
docker run -d --memory=100m -p 80:5000 --name flask-container iti-flask-lab2
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
docker tag iti-flask-lab2 ziyadtarek99/iti-flask-lab2:latest
```

### **3. Push the Image**
```sh
docker push ziyadtarek99/iti-flask-lab2:latest
```

---

## **Dockerfile Explanation**
This Dockerfile builds a lightweight Flask application container.

```dockerfile
FROM python:3.9-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "routes.py"]
```

---

## **License**
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
