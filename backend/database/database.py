from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from backend.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


def init_db():
    Base.metadata.create_all(bind=engine)
    

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
