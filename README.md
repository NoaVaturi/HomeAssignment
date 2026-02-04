# Python API with Kubernetes & Ingress

A production-ready demonstration of a Python Flask API running on Kubernetes (Minikube). 
The project showcases secure secret management, automated logging, and advanced traffic routing using Ingress.

---

## 🚀 Features

**Python Flask API**: Validates a secret value via POST requests.

**Kubernetes Architecture**: Deployment with 2 replicas for high availability.

**Security**: Uses Kubernetes Secrets to store sensitive data (no hardcoded credentials).

**Logging**: Persistent logging of successful access attempts within the container.

**Traffic Management**: Configured Ingress controller for modern URL-based routing.

---

## 🛠 Prerequisites

**Minikube** installed.

**kubectl** installed.

**Docker** installed.

---

## 📦 Setup & Installation

**1. Start Minikube & Enable Addons:**

minikube start
minikube addons enable ingress

**2. Configure Docker Environment:**
To build the image directly inside Minikube's Docker daemon:

eval $(minikube docker-env)

**3. Build the Image:**

docker build -t python-api:latest .

**4. Deploy to Kubernetes:**
Before deploying, create the secret file from the example:
1. Copy `k8s/secret.yaml.example` to `k8s/secret.yaml`.
2. Update the `API_SECRET_VALUE` with your base64 encoded secret.
3. Apply the manifests:

kubectl apply -f k8s/

---

## 🌍 Accessing the API
Since i am using **Ingress** on a local machine, i need to create a network tunnel:

**1. Open a new terminal and run:**

minikube tunnel

**2. Send a test request:**

curl -X POST http://localhost/validate \
     -H "Content-Type: application/json" \
     -d '{"value": "super-secret-123"}'

---

## 🔍 Verification & Logs

**Check Application Logs:**
To see the internal success.log file created by the app:

kubectl exec -it <POD_NAME> -- cat /app/success.log

**View Pod Status:**

kubectl get pods
kubectl get ingress

---

## 💡 Discussion Points 
**Secret Management**: I used K8s Secrets to decouple configuration from code. In a cloud environment, I would integrate with AWS Secrets Manager using External Secrets Operator.

**Observability**: Successes are logged to a file. For production, stream these logs to CloudWatch for persistence.