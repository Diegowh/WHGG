from __future__ import annotations
from src.models.league.league_entry import LeagueEntry
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from src.models.base import Base
from src.models.match.match import Match


class Account(Base):
    __tablename__ = "account"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    league_entries: Mapped[list[LeagueEntry]] = relationship(back_populates="account", cascade="all, delete-orphan")
    matches: Mapped[list[Match]] = relationship(back_populates="account")
    
    puuid: Mapped[str] = mapped_column(String(78), unique=True, index=True)
    summonerId: Mapped[str] = mapped_column(String(63), unique=True, index=True)
    accountId: Mapped[str] = mapped_column(String(56), unique=True)
    gameName: Mapped[str]
    tagLine: Mapped[str]
    profileIconId: Mapped[int]
    summonerLevel: Mapped[int]
    # Fecha en la que el Summoner fue modificado por ultima vez, especificada en milisegundos desde el epoch
    # Los siguientes eventos actualizaran este timestamp: 
    # cambio de summoner name, cambio de summoner level, cambio de profile icon
    revisionDate: Mapped[int]
    
    def __repr__(self) -> str:
        return (f"Account(puuid={self.puuid!r}, summonerId={self.summonerId!r}, "
                f"accountId={self.accountId!r}, gameName={self.gameName!r}, "
                f"tagLine={self.tagLine!r}, profileIconId={self.profileIconId!r}, "
                f"revisionDate={self.revisionDate!r}, summonerLevel={self.summonerLevel!r}, "
                f"league_entries={self.league_entries!r}, matches={self.matches!r})")