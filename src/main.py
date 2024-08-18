from fastapi import FastAPI
from src.database.database import init_db
from src.api.v1.endpoints import router as api_router


app = FastAPI(title="WH.GG")

init_db()

app.include_router(api_router)