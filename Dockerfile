FROM python:3.12.1-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo pyproject.toml y poetry.lock para instalar las dependencias
COPY pyproject.toml poetry.lock conftest.py ./

# Instala Poetry
RUN pip install poetry

# Instala las dependencias del proyecto sin instalar el entorno virtual
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copia el código del backend al contenedor
COPY backend/ ./backend

# Define el comando para ejecutar tu aplicación usando FastAPI
CMD ["poetry", "run", "fastapi", "run", "backend/main.py", "--port", "8000"]