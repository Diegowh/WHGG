"""
Encargado de las operaciones CRUD de la base de datos
"""

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.config import Settings


class DBController:

    def __init__(self, settings: 'Settings') -> None:
        self._settings = settings
        self._engine = self._create_engine()
        self._create_session_factory()

    
    def _create_engine(self) -> Engine:
        """Crea un Engine de SQLAlchemy usando los settings"""
        db_url = f"postgresql://{self._settings.DB_USER}:{self._settings.DB_PASSWORD}@{self._settings.DB_HOST}:{self._settings.DB_PORT}/{self._settings.DB_NAME}"
        return create_engine(db_url)
    
    def _create_session_factory(self):
        ...