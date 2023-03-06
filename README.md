# k8s-demo

Build Docker image: docker build -t <registry/repository:tag> .

Push Docker image: docker push <registry/repository:tag>

Setup kubernetes cluster
  - minikube (locally)
  - obtain kubeconfig from cloud provider
  - create namespace for deployment: `kubectl create ns <name>` or `kubectl apply -f manifests/namespace.yaml`
  - install demo application using helm: `helm install -n <namespace> <release_name> ./charts/demo` or apply manifests with kubectl
