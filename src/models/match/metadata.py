from __future__ import annotations
from src.models.account.account import Account
from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer



class Metadata(Base):
    __tablename__ = "metadata"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    match_id: Mapped
    dataVersion: Mapped[str]
    matchId: Mapped[str]
    participants: Mapped[list[str]]
