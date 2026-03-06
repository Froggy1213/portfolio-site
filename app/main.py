from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from starlette.middleware.sessions import SessionMiddleware  
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware  

from app.database import engine
from app.admin import setup_admin
from app.config import settings

from app.routers.pages import router as pages_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        pass
    yield

app = FastAPI(lifespan=lifespan)

# --- MIDDLEWARE ---
# 1. Чтобы админка понимала, что мы работаем через HTTPS (чинит CSS/JS)
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")

# 2. Чтобы работала авторизация в админке (хранение кук)
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

# --- СТАТИКА И АДМИНКА ---
app.mount("/static", StaticFiles(directory="static"), name="static")
setup_admin(app, engine)

# --- МАРШРУТЫ ---
# Подключаем все наши эндпоинты (/, /projects, robots.txt и т.д.)
app.include_router(pages_router)