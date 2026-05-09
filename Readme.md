# House Price Prediction API

## Project Overview

Built an end-to-end MLOps pipeline that predicts house prices and serves predictions through a production-ready API.

This project evolved from a basic machine learning model into a complete production deployment system:

ML Model → FastAPI → Docker → Kubernetes → Prometheus → Grafana → CI/CD

Users can send house details such as living area, overall quality, and garage capacity to receive real-time house price predictions.

---

# Features

## Machine Learning
- Data preprocessing using Pandas
- Missing value handling
- Feature engineering
- Decision Tree model training
- Random Forest model training
- Hyperparameter tuning
- Model persistence using Joblib

## Model Performance
- Random Forest selected as final model
- Evaluated using MAE (Mean Absolute Error)
- Best model saved using Joblib

## Backend/API
- REST API built using FastAPI
- Input validation using Pydantic
- Real-time prediction endpoint
- Swagger API documentation

## Deployment & DevOps
- Containerized using Docker
- Deployed on Render
- Kubernetes deployment using Minikube
- Service exposure using Kubernetes Services
- CI/CD pipeline using GitHub Actions

## Monitoring & Observability
- Prometheus metrics integration
- API monitoring endpoint (/metrics)
- Grafana dashboard visualization
- Request monitoring
- Error monitoring
- Latency tracking
- CPU monitoring
- Memory monitoring

---

# Tech Stack

### ML
- Python
- Pandas
- Scikit-learn
- Joblib

### Backend
- FastAPI
- Pydantic
- Uvicorn

### DevOps
- Docker
- Kubernetes
- GitHub Actions

### Monitoring
- Prometheus
- Grafana

### Cloud
- Render

### Version Control
- Git
- GitHub

---

# Dataset
Dataset Used: Kaggle House Prices Dataset
File Used: train.csv
Target Variable: SalePrice

---

# API Endpoints

## GET /
Checks whether API is running

Sample Response:
{
  "message": "House Price Prediction API is running"
}

## POST /predict

Sample Input:
{
  "GrLivArea": 1500,
  "OverallQual": 7,
  "GarageCars": 2
}

Sample Output:
{
  "predicted_price": 149111.58
}

---

# Monitoring Endpoint

GET /metrics

Tracks:
- Total requests
- Error rate
- Latency
- CPU usage
- Memory usage

---

# Docker Commands
docker build -t house-price-api .
docker run -p 8000:8000 house-price-api

API Docs:
http://localhost:8000/docs

---

# Kubernetes Commands
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods
kubectl get services
minikube service house-price-service --url

---

# Prometheus
Download: https://prometheus.io/download/
Run: prometheus.exe
Dashboard: http://localhost:9090

---

# Grafana
Download: https://grafana.com/grafana/download
Dashboard: http://localhost:3000
Default Login:
Username: admin
Password: admin

---

# Live Deployment
https://house-price-api-ob1n.onrender.com
https://house-price-api-ob1n.onrender.com/docs

---

# Production Architecture

Client Request
    ↓
FastAPI API
    ↓
ML Model
    ↓
Docker Container
    ↓
Kubernetes Deployment
    ↓
Prometheus Monitoring
    ↓
Grafana Dashboard
    ↓
CI/CD Pipeline

---

# Key Learning Outcomes
- End-to-end MLOps pipeline development
- API development
- Docker containerization
- Kubernetes orchestration
- Monitoring & observability
- CI/CD automation
- Production debugging
- Cloud deployment fundamentals
