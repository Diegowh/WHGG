from __future__ import annotations
from src.models.match.match import Match
from src.models.account.account import Account
from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer
from src.models.match.participant import Participant



class Metadata(Base):
    __tablename__ = "metadata"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    match_id: Mapped[int] = mapped_column(ForeignKey("match.id"))
    match: Mapped[Match] = relationship(back_populates="metadata", uselist=False)

    participants: Mapped[list[Participant]] = relationship(back_populates="metadata")

    participants: Mapped[list[str]]    
    dataVersion: Mapped[str]