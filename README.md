# Adilet Iusupov | Personal Portfolio

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql&logoColor=white)

A high-performance personal portfolio website and blog built with a focus on backend architecture, clean design, and scalability. Designed to showcase engineering projects and professional services.

## 🚀 Features

-   **Modern Stack:** Built with Python (FastAPI) and SQLAlchemy (Async).
-   **Admin Panel:** Integrated `sqladmin` interface for managing projects without touching the DB.
-   **Server-Side Rendering:** SEO-friendly templates using Jinja2.
-   **Responsive Design:** Styled with TailwindCSS with a custom dark mode aesthetic.
-   **Production Ready:** Dockerized setup with Nginx/Caddy proxy support (handles HTTPS and mixed content correctly).
-   **Secure:** Session-based authentication for the admin area.

## 🛠️ Tech Stack

-   **Backend:** Python 3.11, FastAPI, Starlette
-   **Database:** PostgreSQL (Asyncpg + SQLAlchemy)
-   **Frontend:** HTML5, Jinja2, TailwindCSS (CDN)
-   **Infrastructure:** Docker, Docker Compose
-   **Admin Interface:** SQLAdmin

## 📂 Project Structure

.
├── app/
│   ├── admin.py        # Admin panel configuration
│   ├── config.py       # Environment settings (Pydantic)
│   ├── database.py     # DB connection & session logic
│   ├── main.py         # App entry point & routing
│   └── models.py       # SQLAlchemy database models
├── static/
│   ├── images/         # Static assets
│   └── uploads/        # User-uploaded project images
├── templates/          # Jinja2 HTML templates
├── docker-compose.yml  # Container orchestration
└── requirements.txt    # Python dependencies


## ⚡ Getting Started (Local Development)
Prerequisites

    Docker & Docker Compose

    Git

Installation

    Clone the repository:
    Bash

git clone [https://github.com/Froggy1213/portfolio-site.git](https://github.com/Froggy1213/portfolio-site.git)
cd portfolio-site

Configure Environment: Create a .env file in the root directory:
Ini, TOML

# .env example
DB_USER=postgres
DB_PASS=postgres
DB_HOST=db
DB_PORT=5432
DB_NAME=portfolio_db

SECRET_KEY=change_this_to_something_secure
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin
DEBUG=True

Run with Docker:
Bash

    docker-compose up --build

        The site will be available at http://localhost:8000.

        The admin panel is at http://localhost:8000/admin.

🚢 Deployment

The project is designed to be deployed on a Linux server using Docker.

    Pull changes on the server:
    Bash

git pull origin main

Restart containers:
Bash

    docker-compose up -d --build

📬 Contact

Adilet Iusupov - Backend Software Engineer

    Email: adikyu202@gmail.com

    LinkedIn: Adilet Iusupov

    GitHub: Froggy1213