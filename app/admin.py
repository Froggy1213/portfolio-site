import os
import uuid
import shutil
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from wtforms import FileField  # Для загрузки файлов
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

    column_list = [Project.id, Project.title, Project.is_active, Project.image_url]
    form_columns = [
        Project.title, 
        Project.description, 
        Project.tech_stack, 
        Project.github_link, 
        Project.demo_link, 
        Project.is_active, 
        Project.order
    ]

    form_extra_fields = {
        "new_image": FileField("Upload Image")
    }


    # Магия сохранения файла
    async def on_model_change(self, data, model, is_created, request):
        # Получаем файл из формы
        file = data.get("new_image")

        # Если файл был загружен (у него есть имя)
        if file and getattr(file, 'filename', None):
            # 1. Генерируем уникальное имя (чтобы файл "me.jpg" не затер другой "me.jpg")
            ext = file.filename.split(".")[-1]
            unique_name = f"{uuid.uuid4()}.{ext}"

            # 2. Создаем папку, если её нет
            upload_dir = "static/uploads"
            os.makedirs(upload_dir, exist_ok=True)

            # 3. Полный путь к файлу
            file_path = os.path.join(upload_dir, unique_name)

            # 4. Сохраняем файл на диск
            # Читаем содержимое и пишем в файл
            content = await file.read()
            with open(file_path, "wb") as f:
                f.write(content) 

            # 5. Записываем в базу данных ССЫЛКУ на этот файл
            # Именно это значение пойдет в колонку image_url
            model.image_url = f"/static/uploads/{unique_name}"



# Функция инициализации
def setup_admin(app, engine):
    authentication_backend = AdminAuth(secret_key=settings.SECRET_KEY)

    admin = Admin(
        app, 
        engine, 
        authentication_backend=authentication_backend
        templates_dir='templates'
    )
    
    admin.add_view(ProjectAdmin)
    