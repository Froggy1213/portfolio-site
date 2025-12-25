# Используем легкую версию Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Запрещаем Python создавать .pyc файлы и буферизировать вывод (важно для логов)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем системные зависимости (нужны для сборки некоторых python-библиотек)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем библиотеки
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Копируем весь код проекта внутрь контейнера
COPY . .

# Команда запуска (на сервере используем gunicorn для надежности или uvicorn напрямую)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]