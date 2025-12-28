import os
import uuid
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from wtforms import FileField
from markupsafe import Markup
from app.models import Project
from app.config import settings

# --- 1. Авторизация ---
class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

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

# --- 2. Настройка Проектов ---
class ProjectAdmin(ModelView, model=Project):
    name = "Project"
    name_plural = "Projects"
    icon = "fa-solid fa-code"

    # === СПИСОК (Таблица) ===
    column_list = [Project.id, Project.title, Project.is_active, Project.image_url]

    # Форматтер для картинок в таблице
    @staticmethod
    def image_formatter(model, attribute):
        try:
            key = attribute.key if hasattr(attribute, "key") else str(attribute)
            value = getattr(model, key, None)
            if value:
                return Markup(f'<img src="{value}" width="50" style="border-radius: 4px; border: 1px solid #ccc;">')
        except Exception:
            pass
        return ""

    column_formatters = {
        Project.image_url: image_formatter
    }

    # === ФОРМА (Создание / Редактирование) ===
    form_columns = [
        Project.title,
        Project.description,
        Project.image_url,  
        Project.tech_stack,
        Project.github_link,
        Project.demo_link,
        Project.is_active,
        Project.order
    ]

    # ВАЖНО: Превращаем текстовое поле image_url в поле загрузки файла
    form_overrides = {
        "image_url": FileField
    }
    
    # Меняем подпись кнопки
    form_args = {
        "image_url": {"label": "Upload Project Image"}
    }

    # Логика сохранения
    async def on_model_change(self, data, model, is_created, request):
        # Получаем объект файла из поля image_url
        file = data.get("image_url")

        # Если это файл (UploadFile) и у него есть имя
        if file and hasattr(file, "filename") and file.filename:
            # 1. Генерируем имя
            ext = file.filename.split(".")[-1]
            unique_name = f"{uuid.uuid4()}.{ext}"

            # 2. Создаем папку
            upload_dir = "static/uploads"
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, unique_name)

            # 3. Сохраняем файл
            content = await file.read()
            with open(file_path, "wb") as f:
                f.write(content)

            # 4. ВАЖНО: Подменяем объект файла на строку пути для базы данных
            data["image_url"] = f"/static/uploads/{unique_name}"
            model.image_url = f"/static/uploads/{unique_name}"
        
        # Если файл НЕ загружали, но мы редактируем проект
        elif not is_created and model.image_url:
            # Оставляем старую ссылку (удаляем пустой объект файла из данных, чтобы не стереть путь)
             if "image_url" in data:
                 del data["image_url"]

# --- 3. Инициализация ---
def setup_admin(app, engine):
    authentication_backend = AdminAuth(secret_key=settings.SECRET_KEY)
    
    admin = Admin(
        app, 
        engine, 
        authentication_backend=authentication_backend,
    )
    
    admin.add_view(ProjectAdmin)