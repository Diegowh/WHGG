from __future__ import annotations
from dataclasses import dataclass
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.models.account.account import Account


class LeagueEntry(Base):
    __tablename__ = "league_entry"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    leagueId: Mapped[String]
    queueType: Mapped[String]
    tier: Mapped[String]
    rank: Mapped[String]
    summonerId: Mapped[String] = mapped_column(String, ForeignKey("account.summonerId"))
    leaguePoints: Mapped[Integer]
    wins: Mapped[Integer]
    losses: Mapped[Integer]
    hotStreak: Mapped[Boolean]
    veteran: Mapped[Boolean]
    freshBlood: Mapped[Boolean]
    inactive: Mapped[Boolean]
    
    
    account: Mapped[Account] = relationship(back_populates="league_entries")
    
    def __repr__(self) -> str:
        return f"LeagueEntry(id={self.id!r}, summonerId={self.summonerId!r}, tier={self.tier!r}, rank={self.rank!r})"