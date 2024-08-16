from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import src.database.models as models
import src.database.schemas as schemas

from src.database.database import Base, engine, SessionLocal
from src.database import crud



Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="WH.GG"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
schemas.Account

@app.get("/accounts/", response_model=list[schemas.Account])
def get_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    accounts = crud.get_accounts(db, skip=skip, limit=limit)
    return accounts