from fastapi import FastAPI
from backend.database.database import init_db
from backend.api.v1.endpoints import router as api_router


app = FastAPI(title="WH.GG")

init_db()

app.include_router(api_router)