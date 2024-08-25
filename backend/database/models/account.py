'''
Este módulo contiene la clase `Account` que extiende de `sqlalchemy.orm.DeclarativeBase`
y representa un modelo de tabla
'''

from typing import Optional

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

from backend.database.database import Base

from backend.database.models.champion_stats import ChampionStats
from backend.database.models.league_entry import LeagueEntry
from backend.database.models.match import Match


class Account(Base):  # pylint: disable=too-few-public-methods
    """Representa un modelo de Account en la base de datos.

    Esta clase extiende de `sqlalchemy.orm.DeclarativeBase`
    y se mapea a la tabla `account` en la base de datos.

    La clase `Account` contiene información sobre una cuenta de Riot Games.
    """
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    league_entries: Mapped[list["LeagueEntry"]] = relationship(
        back_populates="account",
        cascade="all, delete-orphan"
    )
    matches: Mapped[list["Match"]] = relationship(
        back_populates="account",
        cascade="all, delete-orphan"
    )
    champion_stats: Mapped[list["ChampionStats"]] = relationship(
        back_populates="account",
        cascade="all, delete-orphan"
    )

    puuid: Mapped[str] = mapped_column(String(78), unique=True, index=True)
    summoner_id: Mapped[str] = mapped_column(String(63), unique=True, index=True)
    account_id: Mapped[str] = mapped_column(String(56), unique=True)
    game_name: Mapped[str]
    tag_line: Mapped[str]
    profile_icon_id: Mapped[int]
    summoner_level: Mapped[int]
    last_update: Mapped[Optional[int]]

    __table_args__ = (
        UniqueConstraint("game_name", "tag_line", name="_game_name_tag_line_uc"),
    )

    def __repr__(self) -> str:
        attrs = [
            f"puuid={self.puuid!r}",
            f"summonerId={self.summoner_id!r}",
            f"accountId={self.account_id!r}",
            f"gameName={self.game_name!r}",
            f"tagLine={self.tag_line!r}",
            f"profileIconId={self.profile_icon_id!r}",
            f"summonerLevel={self.summoner_level!r}",
            f"lastUpdate={self.last_update!r}",
            f"league_entries=[{', '.join(repr(le) for le in self.league_entries)}]",
            f"matches=[{', '.join(repr(m) for m in self.matches)}]",
            f"champion_stats=[{', '.join(repr(cs) for cs in self.champion_stats)}]"
        ]
        return f"Account({', '.join(attrs)})"
