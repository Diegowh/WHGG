from __future__ import annotations
from src.models.base import Base
from sqlalchemy import Mapped, true
from sqlalchemy.orm import Mapped, mapped_column
from src.models.match.metadata import Metadata
from src.models.match.info import Info



class Match(Base):
    
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(primary_key=true, unique=true, autoincrement=true, index=true)
    metadata: Mapped[Metadata]
    info: Mapped[Info]