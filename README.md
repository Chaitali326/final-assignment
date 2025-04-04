# Final Assignment - SL III

## 📌 Project Overview

This is the final assignment for Software Lab III, showcasing a multi-container Dockerized web application. The project consists of:

- A **Django application** for backend logic, item management, and serving web pages.
- A **Flask microservice** that runs alongside Django and serves a simple route.
- A **Docker Compose** setup to build and run both services.
- A **Jenkinsfile** for CI/CD integration (build automation pipeline).

---

## 🛠️ Technologies Used

- Python 3.10  
- Django (for main app logic and item management)  
- Flask (microservice)  
- Docker & Docker Compose  
- Jenkins (CI/CD Pipeline)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Chaitali326/final-assignment.git
cd final-assignment
2. Build and Run with Docker Compose
bash
Copy
Edit
docker-compose up --build
This builds and runs both the Django and Flask containers.

🎈 App URLs
Django App: http://localhost:8000

Flask App: http://localhost:5000

📂 Folder Structure
php
Copy
Edit
final-assignment/
├── django_app/             # Django project folder
│   ├── Dockerfile
│   ├── manage.py
│   └── ...
│
├── flask_app/              # Flask app folder
│   ├── Dockerfile
│   ├── app.py
│   └── ...
│
├── docker-compose.yml      # Docker Compose file
├── Jenkinsfile             # CI/CD Jenkins pipeline
└── README.md               # This file
🧩 Django Migrations
Before running the server, make sure to apply migrations:

bash
Copy
Edit
docker exec -it final-assignment-django-1 python manage.py makemigrations
docker exec -it final-assignment-django-1 python manage.py migrate
⚙️ Jenkins Integration
This project includes a Jenkinsfile which automates the build and deployment pipeline.

Jenkins Pipeline Overview
Pulls the latest code from GitHub

Builds Docker images for Django and Flask

Runs both containers using Docker Compose

Can be extended to run unit tests and perform health checks

To use it:
Set up a Jenkins job with GitHub integration

Use a Docker-enabled Jenkins agent

Add GitHub credentials and allow pipeline execution from your Jenkins dashboard

👩‍💻 Author
Chaitali326
This project was developed as part of the Software Lab III final assignment.