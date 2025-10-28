# QuakeWatch2 - GitOps Deployment with ArgoCD and Monitoring Stack

This project automates the deployment of the `quakewatch2` Python web application using **GitOps principles** via **ArgoCD**, and integrates observability through **Prometheus**, **Grafana**, and alerting rules.

---

## 📦 Project Structure

```bash
quakewatch2/
├── chart/                    # Helm chart for application
│   ├── templates/            # Kubernetes resources
│   ├── Chart.yaml
│   └── values.yaml
├── manifests/
│   ├── quakewatch2-app.yaml  # ArgoCD Application manifest
│   ├── namespace.yaml
│   ├── prometheus-rules.yaml
│   └── service-monitor.yaml
├── dashboards/
│   └── quakewatch2-grafana-dashboard.json
└── README.md
🚀 GitOps with ArgoCD
Prerequisites

Kubernetes cluster (e.g., Minikube)

ArgoCD installed in namespace argocd

ArgoCD CLI (argocd)

This repo is pushed to a Git provider (GitHub, GitLab, etc.)

Install ArgoCD (Optional)
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

Access ArgoCD UI
kubectl port-forward svc/argocd-server -n argocd 8080:443


Then go to: https://localhost:8080

Retrieve Admin Password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

🧩 Application Deployment
1. Create Namespace
kubectl apply -f manifests/namespace.yaml

2. Apply ArgoCD Application Manifest
kubectl apply -f manifests/quakewatch2-app.yaml


ArgoCD will automatically deploy and sync the app from your Git repo.

📊 Monitoring with Prometheus & Grafana
Access Grafana
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80


Login with:

Username: admin

Password: run kubectl get secret --namespace monitoring monitoring-grafana -o jsonpath="{.data.admin-password}" | base64 -d

Upload Dashboard

Open Grafana → Dashboards → Import

Upload dashboards/quakewatch2-grafana-dashboard.json

Prometheus Metrics

Sample queries:

rate(container_cpu_usage_seconds_total[5m])

container_memory_usage_bytes

kube_pod_container_status_restarts_total

kubelet_volume_stats_available_bytes

🚨 Alerting
Apply Alert Rules
kubectl apply -f manifests/prometheus-rules.yaml -n monitoring

Included Rules:

Pod crashlooping

High CPU usage

High memory usage

Cluster health degraded



Grafana dashboard with metrics

Sample alert firing
