<div align="center">

# Adilet Iusupov | Personal Portfolio

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

<p align="center">
  <strong>High-performance portfolio & blog engine for Backend Engineers.</strong><br>
  Built with a focus on clean architecture, scalability, and modern DevOps practices.
</p>

[View Demo](https://adiletyu.com) • [Report Bug](https://github.com/Froggy1213/portfolio-site/issues) • [Request Feature](https://github.com/Froggy1213/portfolio-site/issues)

</div>

---

## 🚀 About The Project

This project is not just a static site; it's a fully dockerized web application designed to showcase engineering skills. It features a custom admin panel, server-side rendering for SEO, and a robust backend architecture using asynchronous Python.

### Key Features

* **⚡ Modern Backend:** Built with **FastAPI** and **SQLAlchemy (Async)** for high performance.
* **🛡️ Secure Admin:** Integrated **SQLAdmin** interface with session-based authentication.
* **🎨 Responsive UI:** Styled with **TailwindCSS** (Dark Mode aesthetic).
* **🐳 Production Ready:** Fully containerized with **Docker Compose**.
* **🔒 Proxy Support:** Configured to work behind Nginx/Caddy with correct HTTPS handling.

---

## 🛠️ Tech Stack

| Category | Technologies |
| :--- | :--- |
| **Core** | ![Python](https://img.shields.io/badge/Python-3.11-blue) |
| **Framework** | ![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688) ![Starlette](https://img.shields.io/badge/Starlette-Ready-black) |
| **Database** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Async-red) |
| **Frontend** | ![Jinja2](https://img.shields.io/badge/Jinja2-Templates-b41717) ![Tailwind](https://img.shields.io/badge/TailwindCSS-3.0-38B2AC) |
| **DevOps** | ![Docker](https://img.shields.io/badge/Docker-Compose-2496ED) ![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420) |

---

## 📂 Project Structure

```bash
.
├── app/
│   ├── admin.py        # Admin panel configuration & auth
│   ├── config.py       # Pydantic settings management
│   ├── database.py     # Async DB connection logic
│   ├── main.py         # Application entry point
│   └── models.py       # SQLAlchemy ORM models
├── static/
│   ├── images/         # Assets & Favicons
│   └── uploads/        # User-uploaded content (Git ignored)
├── templates/          # Jinja2 HTML templates
├── docker-compose.yml  # Orchestration
└── requirements.txt    # Dependencies

