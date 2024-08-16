from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.database.models.champion_stats import ChampionStats
    from src.database.models.league_entry import LeagueEntry
    from src.database.models.match import Match
    

class Account(Base):
    __tablename__ = "account"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    league_entries: Mapped[list["LeagueEntry"]] = relationship(back_populates="account", cascade="all, delete-orphan")
    matches: Mapped[list["Match"]] = relationship(back_populates="account", cascade="all, delete-orphan")
    champion_stats: Mapped[list["ChampionStats"]] = relationship(back_populates="account", cascade="all, delete-orphan")

    puuid: Mapped[str] = mapped_column(String(78), unique=True, index=True)
    summoner_id: Mapped[str] = mapped_column(String(63), unique=True, index=True)
    account_id: Mapped[str] = mapped_column(String(56), unique=True)
    game_name: Mapped[str]
    tag_line: Mapped[str]
    profile_icon_id: Mapped[int]
    summoner_level: Mapped[int]
    last_update: Mapped[int]
    
    def __repr__(self) -> str:
        return (f"Account(puuid={self.puuid!r}, summonerId={self.summoner_id!r}, "
                f"accountId={self.account_id!r}, gameName={self.game_name!r}, "
                f"tagLine={self.tag_line!r}, profileIconId={self.profile_icon_id!r}, "
                f"lastUpdate={self.last_update!r}, summonerLevel={self.summoner_level!r}, "
                f"league_entries={self.league_entries!r}, matches={self.matches!r})")