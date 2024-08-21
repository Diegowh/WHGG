from fastapi import FastAPI

from backend.api.v1.endpoints import router as api_router
from backend.database.database import init_db

app = FastAPI(title="WHGG")

init_db()

app.include_router(api_router)