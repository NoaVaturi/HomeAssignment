# Python API with Kubernetes & Ingress

A production-ready demonstration of a Python Flask API running on Kubernetes (Minikube).
The project showcases secure secret management, automated logging, and advanced traffic routing using Ingress.

---

## 🚀 Features

* **Python Flask API**: Validates a secret value via POST requests.
* **Kubernetes Architecture**: Deployment with 2 replicas for high availability.
* **Security**: Uses Kubernetes Secrets to store sensitive data.
* **Logging**: Persistent logging of successful access attempts within the container.
* **Traffic Management**: Configured Ingress controller for modern URL-based routing.

---

## 🛠 Prerequisites

* **Minikube** installed.
* **kubectl** installed.
* **Docker** installed.

---

## 📦 Setup & Installation

**1. Start Minikube & Enable Addons:**

```bash
minikube start
minikube addons enable ingress
```


**2. Configure Docker Environment:**

```bash
eval $(minikube docker-env)
```


**3. Build the Image:**

```bash
docker build -t python-api:v1 .
```


**4. Deploy to Kubernetes:**

Before deploying, create the secret file from the example:

*Copy k8s/secret.yaml.example to k8s/secret.yaml.

*Update the API_SECRET_VALUE with your base64 encoded secret.

*Apply the manifests:

```bash
kubectl apply -f k8s/
```

---

## 🌍 Accessing the API
Since I am using Ingress on a local machine, I need to create a network tunnel:

1. Open a new terminal and run:

```bash
minikube tunnel
```


2. Send a test request:

```bash
curl -X POST http://localhost/validate \
     -H "Content-Type: application/json" \
     -d '{"value": "your-secret-here"}'
```

---

## 🔍 Verification & Logs
Check Application Logs:

```bash
kubectl exec -it <POD_NAME> -- cat /app/success.log
```


View Status:

```bash
kubectl get pods
kubectl get ingress
```

---

## 💡 Discussion Points
**Secret Management**: I used K8s Secrets to decouple configuration from code. In a cloud environment, I would integrate with AWS Secrets Manager.

**Ingress Routing**: I implemented Ingress (Port 80) to simulate production-grade traffic management instead of using temporary NodePorts.

**Observability**: Successes are logged to a file. For production, I'd stream these logs to a centralized solution like CloudWatch.