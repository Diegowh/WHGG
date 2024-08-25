'''
Este módulo se encarga de la configuración y gestión de la base de datos

Contiene la configuración necesaria para conectar con la base de datos,
definir el modelo para las tablas de SQLAlchemy y crear sesiones para
interactuar con la base de datos. 
También proporciona funciones para inicializar y gestionar el ciclo de vida
de las sesiones.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from backend.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(engine)


class Base(DeclarativeBase):  # pylint: disable=too-few-public-methods
    """Clase base para la definición de modelos SQLAlchemy."""


def init_db():
    """Crea todas las tablas en la base de datos basadas en los modelos
    registrados en `Base`
    """
    Base.metadata.create_all(bind=engine)


def get_db():
    """Factory de `SessionLocal`
    Crea y proporciona una nueva sesión de base de datos 
    en el contexto de una operación y cierra la sesión una vez completada.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
