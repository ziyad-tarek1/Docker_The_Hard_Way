
# Kubernetes Voting App

## Description

The **Kubernetes Voting App** is a simple deployment of a voting application using pre-configured images from [KodeKloud](https://www.kodekloud.com/). This project demonstrates how to set up a multi-service architecture using Kubernetes, including services for PostgreSQL, Redis, and the voting application itself.

## Project Structure

```plaintext
.
├── postgres-deploy.yaml
├── postgres-service.yaml
├── redis-deploy.yaml
├── redis-service.yaml
├── result-app-deploy.yaml
├── result-app-service.yaml
├── voting-app-deploy.yaml
├── voting-app-service.yaml
└── worker-app-deploy.yaml
```

- **postgres-deploy.yaml**: Deployment configuration for PostgreSQL.
- **postgres-service.yaml**: Service configuration for PostgreSQL.
- **redis-deploy.yaml**: Deployment configuration for Redis.
- **redis-service.yaml**: Service configuration for Redis.
- **result-app-deploy.yaml**: Deployment configuration for the result application.
- **result-app-service.yaml**: Service configuration for the result application.
- **voting-app-deploy.yaml**: Deployment configuration for the voting application.
- **voting-app-service.yaml**: Service configuration for the voting application.
- **worker-app-deploy.yaml**: Deployment configuration for the worker application.

## Prerequisites

1. **Kubernetes Cluster**: Ensure you have a Kubernetes cluster running. You can use:
   - Minikube
   - Docker Desktop
   - Any cloud provider (e.g., Google Kubernetes Engine, Amazon EKS, Azure AKS)

2. **kubectl**: Install the Kubernetes command-line tool, `kubectl`, to interact with your cluster.

## Deployment Instructions

1. **Navigate to the Project Directory**:
   Open your terminal and navigate to the directory containing the Kubernetes manifests:
   ```bash
   cd k8s-voting-app
   ```

2. **Apply the Kubernetes Manifests**:
   Use the following commands to apply the necessary Kubernetes manifests:
   ```bash
   kubectl apply -f postgres-deploy.yaml
   kubectl apply -f postgres-service.yaml
   kubectl apply -f redis-deploy.yaml
   kubectl apply -f redis-service.yaml
   kubectl apply -f voting-app-deploy.yaml
   kubectl apply -f voting-app-service.yaml
   kubectl apply -f result-app-deploy.yaml
   kubectl apply -f result-app-service.yaml
   kubectl apply -f worker-app-deploy.yaml
   ```

## Accessing the Application

After deploying the services, you can access the application using the appropriate service endpoints. Depending on your Kubernetes setup, you may need to use `kubectl port-forward` or expose the services via a LoadBalancer or Ingress.

### Example of Port Forwarding

To access the voting application, you can use port forwarding:
```bash
kubectl port-forward service/voting-app-service 8080:80
```

## Conclusion

This project provides a simple yet effective way to deploy a voting application using Kubernetes. By following the instructions above, you can set up the application and access it through the defined services.


### 💡 Contributors
    - Ziyad Tarek Saeed - Author and Maintainer.

Happy coding! 🚀
