# Deploy Flask app with Kubernetes

* At first, install minikube and kubectl in your local machine.
* Run `./create_secret.sh` to create a secret for the app.
* Run `kubectl apply -f deployment-service.yaml` to deploy the app to minikube cluster.
* Lastly, run `kubectl delete -f deployment-service.yaml && ./delete-secret.sh` to destroy the app.
