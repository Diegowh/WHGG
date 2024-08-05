from __future__ import annotations
from src.models.base import Base
from sqlalchemy import Mapped, true
from sqlalchemy.orm import Mapped, mapped_column
from src.models.match.participant import Participant
from src.models.match.team import Team



class Info(Base):

    __tablename__ = "info"
    
    id: Mapped[int] = mapped_column(primary_key=true, autoincrement=true, index=true, unique=true)
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

    participants: list[Participant]
    teams: list[Team]