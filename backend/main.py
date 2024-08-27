'''
Módulo que configura y ejecuta la aplicación FastAPI para el backend.

Inicializa la base de datos y configura las rutas de la API.
'''

from fastapi import FastAPI

from backend.api.v1.endpoints import router as api_router
from backend.database.database import init_db
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="WHGG",
    summary="API para obtener los datos de usuarios de League of Legends.",
    version="1.0",
)
init_db()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)
