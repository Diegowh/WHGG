from __future__ import annotations
from src.models.match.match import Match
from src.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.match.participant import Participant
from src.models.match.team import Team



class Info(Base):
    __tablename__ = "info"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    match_id: Mapped[int] = mapped_column(ForeignKey("match.id"))
    match: Mapped[Match] = relationship(back_populates="info", uselist=False)

    participants: Mapped[list[Participant]] = relationship(back_populates="info")

    teams: Mapped[list[Team]] = relationship(back_populates="info")

    endOfGameResult: Mapped[str]
    gameCreation: Mapped[int]
    gameDuration: Mapped[int]
    gameEndTimestamp: Mapped[int]
    gameId: Mapped[int]
    gameMode: Mapped[str]
    gameName: Mapped[str]
    gameStartTimestamp: Mapped[int]
    gameType: Mapped[str]
    gameVersion: Mapped[str]
    mapId: Mapped[int]
    platformId: Mapped[str]
    queueId: Mapped[int]
    tournamentCode: Mapped[str]

