## Kubernetes Solution

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
