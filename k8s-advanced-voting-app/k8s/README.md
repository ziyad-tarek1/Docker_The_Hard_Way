kubectl apply -f pv-pvc.yaml
kubectl apply -f redis-deployment.yaml
kubectl apply -f db-deployment.yaml
kubectl apply -f vote-deployment.yaml
kubectl apply -f result-deployment.yaml
kubectl apply -f worker-deployment.yaml