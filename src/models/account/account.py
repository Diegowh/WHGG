from __future__ import annotations
from typing import List
from src.models.league.league_entry import LeagueEntry
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.models.base import Base


class Account(Base):
    
    __tablename__ = "account"
    
    puuid: Mapped[str] = mapped_column(String(78), primary_key=True, unique=True, index=True)
    summonerId: Mapped[str] = mapped_column(String(63), unique=True, index=True)
    accountId: Mapped[str] = mapped_column(String(56), unique=True, index=True)
    gameName: Mapped[str]
    tagLine: Mapped[str]
    profileIconId: Mapped[int]
     # Date Summoner was last modified specified as epoch milliseconds.
     # The following events will update this timestamp: summoner name change, summoner level change, or profile icon change
    revisionDate: Mapped[int]
    summonerLevel: Mapped[int]
    
    league_entries: Mapped[List[LeagueEntry]] = relationship(
        back_populates="account",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
        return f"Account(puuid={self.puuid!r}, summonerId={self.summonerId!r}, accountId={self.accountId!r}, gameName={self.gameName!r}, tagLine={self.tagLine!r}, profileIconId={self.profileIconId!r}, revisionDate={self.revisionDate!r}, summonerLevel={self.summonerLevel!r}, league={self.league})"
    