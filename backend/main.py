'''
Módulo que configura y ejecuta la aplicación FastAPI para el backend.

Inicializa la base de datos y configura las rutas de la API.
'''

from fastapi import FastAPI

from backend.api.v1.endpoints import router as api_router
from backend.database.database import init_db

app = FastAPI(title="WHGG")
init_db()
app.include_router(api_router)
