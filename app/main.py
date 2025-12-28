from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

# --- НОВЫЕ ИМПОРТЫ ---
from starlette.middleware.sessions import SessionMiddleware  # Для входа в админку
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware  # Для HTTPS (CSS фикс)
# ---------------------

from app.database import engine, Base, get_async_session
from app.models import Project
from app.admin import setup_admin
from app.config import settings  # Импортируем настройки для SECRET_KEY

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

# --- ВАЖНЫЕ ДОБАВЛЕНИЯ ---
# 1. Чтобы админка понимала, что мы работаем через HTTPS (чинит CSS/JS)
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")

# 2. Чтобы работала авторизация в админке (хранение кук)
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
# -------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

setup_admin(app, engine)

@app.get("/")
async def read_root(request: Request, db: AsyncSession = Depends(get_async_session)):
    return templates.TemplateResponse("index.html", {"request":request})

@app.get("/projects")
async def read_projects(request: Request, db: AsyncSession = Depends(get_async_session)):
    # Исправил условие: == True
    query = select(Project).where(Project.is_active == True).order_by(Project.order.desc())
    result = await db.execute(query)
    projects = result.scalars().all()
    
    return templates.TemplateResponse("projects.html", {
        "request": request,
        "projects": projects
    })

@app.get("/robots.txt", include_in_schema=False)
async def get_robots():
    return FileResponse("static/robots.txt")

@app.get("/sitemap.xml", include_in_schema=False)
async def get_sitemap():
    return FileResponse("static/sitemap.xml")