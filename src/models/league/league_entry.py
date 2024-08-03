from __future__ import annotations
from dataclasses import dataclass
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import Base

class LeagueEntry(Base):
    __tablename__ = "league_entry"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    leagueId: Mapped[String] = mapped_column(String)
    queueType: Mapped[String] = mapped_column(String)
    tier: Mapped[String] = mapped_column(String)
    rank: Mapped[String] = mapped_column(String)
    summonerId: Mapped[String] = mapped_column(String, ForeignKey("account.summonerId"))
    leaguePoints: Mapped[Integer] = mapped_column(Integer)
    wins: Mapped[Integer] = mapped_column(Integer)
    losses: Mapped[Integer] = mapped_column(Integer)
    hotStreak: Mapped[Boolean] = mapped_column(Boolean)
    veteran: Mapped[Boolean] = mapped_column(Boolean)
    freshBlood: Mapped[Boolean] = mapped_column(Boolean)
    inactive: Mapped[Boolean] = mapped_column(Boolean)
    
    
    account: Mapped["Account"] = relationship(back_populates="league_entries")
    
    def __repr__(self) -> str:
        return f"LeagueEntry(id={self.id!r}, summonerId={self.summonerId!r}, tier={self.tier!r}, rank={self.rank!r})"