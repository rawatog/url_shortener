# URL Shortener (FastAPI + Jinja2 + SQL + Kubernetes)

A simple and scalable URL shortening service built using **FastAPI**, **Jinja2 templates**, and **SQL database**, with **Kubernetes manifests** for deployment.

---

## 🚀 Features

- Shorten long URLs into compact links
- Redirect shortened URLs to original destinations
- Web UI using Jinja2 templates
- REST API endpoints
- Persistent storage using SQL database
- Containerized deployment support
- Kubernetes-ready manifests

---

## 🏗️ Tech Stack

- **Backend:** FastAPI
- **Frontend:** Jinja2 Templates, HTML/CSS
- **Database:** SQLite / PostgreSQL (configurable)
- **Server:** Uvicorn / Gunicorn
- **Containerization:** Docker
- **Orchestration:** Kubernetes

---

## 📁 Project Structure
url-shortener/
│
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── models.py # Database models
│ ├── schemas.py # Pydantic schemas
│ ├── database.py # DB connection setup
│ ├── crud.py # DB operations
│ ├── templates/ # Jinja2 HTML templates
│ │ ├── index.html
│ │ └── result.html
│ ├── static/ # CSS/JS files
│
├── k8s/
│ ├── deployment.yaml
│ ├── service.yaml 
│ ├── configmap.yaml
│ ├── ingress.yaml  
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .env
