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

## 💡 Discussion Points & Production Considerations

### 🔐 Secret Management
* **Current Implementation**: I used **Kubernetes Secrets** to decouple sensitive data from the application code and injected them as environment variables.
* **Production Approach**: In a cloud-native environment, I would integrate with **AWS Secrets Manager** using an **External Secrets Operator** to ensure advanced encryption and rotation.

### 🌐 Traffic Management (Ingress)
* **Current Implementation**: I implemented an **Ingress Controller** to manage traffic over standard **Port 80**. This provides a unified entry point and simulates production-grade routing.
* **Production Approach**: I would add an **SSL/TLS certificate** for HTTPS (Port 443) and map a real Domain Name via **Route53** to an **External Load Balancer**.

### 📊 Observability & Logging
* **Current Implementation**: Successful requests are logged to a local file within the container for demonstration. 
* **Production Approach**: Since Pods are **ephemeral**, I would configure the application to log to `stdout/stderr`. This allows a logging agent (CloudWatch Agent) to stream logs to a centralized solution like **AWS CloudWatch** for persistence and analysis.

### 📈 Scalability (High Availability)
* **Current Implementation**: The deployment is configured with **2 replicas** to ensure basic availability and demonstrate load balancing.
* **Production Approach**: I would implement a **Horizontal Pod Autoscaler (HPA)** to automatically scale the number of replicas based on CPU/Memory metrics.