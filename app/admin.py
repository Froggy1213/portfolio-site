from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from app.models import Project
from app.config import settings

# --- Настройка безопасности ---
class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        # В реальном проекте пароль и логин хранить в .env!
        if username == settings.ADMIN_USERNAME and password == settings.ADMIN_PASSWORD:
            request.session.update({"token": "admin_token_ok"})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        return bool(token)

# --- Настройка отображения моделей ---
class ProjectAdmin(ModelView, model=Project):
    name = "Project"
    name_plural = "Projects"
    icon = "fa-solid fa-code"

    column_list = [Project.id, Project.title, Project.is_active, Project.order]
    form_columns = [Project.title, Project.slug, Project.description, Project.tech_stack, Project.github_link, Project.image_url, Project.is_active, Project.order]
    
# Функция инициализации
def setup_admin(app, engine):
    authentication_backend = AdminAuth(secret_key=settings.SECRET_KEY)
    admin = Admin(app, engine, authentication_backend=authentication_backend)
    admin.add_view(ProjectAdmin)
    