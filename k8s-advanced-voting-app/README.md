Based on the additional information you've provided about the `container` directory, I've updated the README to include more specific details about the container-only solution, including the structure of the `container` directory and how to use the `docker-compose.yml` file. Here’s the revised README for the **k8s-advanced-voting-app** project:

---

# K8s Advanced Voting App

## Description

The **K8s Advanced Voting App** is a voting application that demonstrates how to deploy a multi-service architecture using both containerization and Kubernetes orchestration. This project includes a container-only solution as well as a Kubernetes solution for deploying the application in a cloud-native environment.

## Project Structure

```plaintext
.
├── container
│   ├── architecture.png
│   ├── docker-compose.yml
│   ├── README.md
│   ├── result
│   └── vote
│   └── worker
├── k8s
│   ├── db-deployment.yaml
│   ├── pv-pvc.yaml
│   ├── README.md
│   ├── redis-deployment.yaml
│   ├── result-deployment.yaml
│   ├── vote-deployment.yaml
│   └── worker-deployment.yaml
└── README.md
```

- **container/**: Contains files related to the container-only solution.
  - **architecture.png**: Diagram illustrating the architecture of the application.
  - **docker-compose.yml**: Docker Compose file to orchestrate the services.
  - **result/**: Directory containing files related to the result service.
  - **vote/**: Directory containing files related to the voting service.
  - **worker/**: Directory containing files related to the worker service.
  
- **k8s/**: Contains Kubernetes deployment files for the application.

## Solutions Overview

### 1. Container-Only Solution

This solution allows you to run the voting application using Docker containers without the need for Kubernetes. It is suitable for local development and testing. To get started with the container-only solution, follow these steps:

1. **Navigate to the Container Directory**:
   ```bash
   cd container
   ```

2. **Build and Run the Application**:
   Use Docker Compose to build and run the application:
   ```bash
   docker-compose up
   ```

3. **Access the Application**:
   Once the containers are running, you can access the application through the specified ports defined in the `docker-compose.yml` file.

### 2. Kubernetes Solution

This solution deploys the voting application using Kubernetes, allowing for better scalability and management of services. To get started with the Kubernetes solution, follow these steps:

1. **Set Up Kubernetes**:
   Ensure you have a Kubernetes cluster running. You can use Minikube, Docker Desktop, or any cloud provider.

2. **Apply the Kubernetes Manifests**:
   Navigate to the `k8s` directory and apply the necessary Kubernetes manifests:
   ```bash
   cd k8s
   kubectl apply -f pv-pvc.yaml
   kubectl apply -f redis-deployment.yaml
   kubectl apply -f db-deployment.yaml
   kubectl apply -f vote-deployment.yaml
   kubectl apply -f result-deployment.yaml
   kubectl apply -f worker-deployment.yaml
   ```

3. **Access the Application**:
   After deploying the services, you can access the application using the appropriate service endpoints.

## Conclusion

This project provides two solutions for deploying the advanced voting application: a container-only solution for local development and a Kubernetes solution for cloud-native deployment. Choose the solution that best fits your needs and follow the respective instructions to get started.

