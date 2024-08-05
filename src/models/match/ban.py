from __future__ import annotations
from src.models.base import Base
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

class Ban(Base):

    __tablename__ = "ban"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    championId: Mapped[int]
    pickTurn: Mapped[int]
