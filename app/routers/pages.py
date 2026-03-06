from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.services.projects import get_active_projects

router = APIRouter(tags=["Pages"])
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/projects")
async def read_projects(request: Request, db: AsyncSession = Depends(get_async_session)):
    projects = await get_active_projects(db)
    return templates.TemplateResponse("projects.html", {
        "request": request,
        "projects": projects
    })

@router.get("/robots.txt", include_in_schema=False)
async def get_robots():
    return FileResponse("static/robots.txt")

@router.get("/sitemap.xml", include_in_schema=False)
async def get_sitemap():
    return FileResponse("static/sitemap.xml")