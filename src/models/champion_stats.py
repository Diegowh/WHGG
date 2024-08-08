from __future__ import annotations

from sqlalchemy import ForeignKey
from src.models.account import Account
from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ChampionStats(Base):
    __tablename__ = "champion_stats"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    account: Mapped[Account] = relationship(back_populates="champion_stats")

    name: Mapped[str]
    kda: Mapped[float]
    kill_avg: Mapped[float]
    death_avg: Mapped[float]
    assist_avg: Mapped[float]
    winrate: Mapped[int]
    games_played: Mapped[int]