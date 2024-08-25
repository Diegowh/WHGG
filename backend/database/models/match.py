'''
Este módulo contiene la clase `Match` que extiende de `sqlalchemy.orm.DeclarativeBase`
y representa un modelo de tabla
'''
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.database import Base

if TYPE_CHECKING:
    from backend.database.models.account import Account
    from backend.database.models.participant import Participant



class Match(Base):  # pylint: disable=too-few-public-methods
    """Representa un modelo de Match en la base de datos.

    Esta clase extiende de `sqlalchemy.orm.DeclarativeBase`
    y se mapea a la tabla `match` en la base de datos.

    La clase `Match` contiene información sobre los datos de una partida jugada
    por el usuario en League of Legends.
    """
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    account_id: Mapped[int] = mapped_column(ForeignKey("account.id", ondelete="CASCADE"))
    account: Mapped["Account"] = relationship(back_populates="matches")

    participants: Mapped[list["Participant"]] = relationship(
        back_populates="match",
        cascade="all, delete-orphan"
    )

    match_id: Mapped[str]
    game_creation: Mapped[BigInteger] = mapped_column(BigInteger)
    game_duration: Mapped[int]
    game_end_timestamp: Mapped[BigInteger] = mapped_column(BigInteger)
    game_mode: Mapped[str]
    game_start_timestamp: Mapped[BigInteger] = mapped_column(BigInteger)
    game_type: Mapped[str]
    game_version: Mapped[str]
    queue_id: Mapped[int]

    assists: Mapped[int]
    champ_level: Mapped[int]
    champion_id: Mapped[int]
    champion_name: Mapped[str]
    deaths: Mapped[int]
    gold_earned: Mapped[int]
    individual_position: Mapped[str]
    item_0: Mapped[int]
    item_1: Mapped[int]
    item_2: Mapped[int]
    item_3: Mapped[int]
    item_4: Mapped[int]
    item_5: Mapped[int]
    item_6: Mapped[int]
    kills: Mapped[int]
    lane: Mapped[str]
    # https://ddragon.leagueoflegends.com/cdn/14.15.1/data/en_US/runesReforged.json
    perk_0: Mapped[int]  # Runa Principal
    perk_1: Mapped[int]  # Runa Secundaria
    puuid: Mapped[str]
    riot_id_game_name: Mapped[str]
    riot_id_tag_line: Mapped[str]
    summoner_1_id: Mapped[int]
    summoner_2_id: Mapped[int]
    summoner_id: Mapped[str]
    team_id: Mapped[int]
    team_position: Mapped[str]
    total_damage_dealt_to_champions: Mapped[int]
    total_minions_killed: Mapped[int]  # Suma neutralMinionsKilled + totalMinionsKilled
    vision_score: Mapped[int]
    wards_placed: Mapped[int]
    win: Mapped[bool]

    def __repr__(self) -> str:
        return (
            f"Match(id={self.id!r}, account_id={self.account_id!r}, "
            f"match_id={self.match_id!r}, game_creation={self.game_creation!r}, "
            f"game_duration={self.game_duration!r}, "
            f"game_end_timestamp={self.game_end_timestamp!r}, "
            f"game_mode={self.game_mode!r}, game_start_timestamp={self.game_start_timestamp!r}, "
            f"game_type={self.game_type!r}, game_version={self.game_version!r}, "
            f"queue_id={self.queue_id!r}, assists={self.assists!r}, "
            f"champ_level={self.champ_level!r}, champion_id={self.champion_id!r}, "
            f"champion_name={self.champion_name!r}, deaths={self.deaths!r}, "
            f"gold_earned={self.gold_earned!r}, individual_position={self.individual_position!r}, "
            f"items=[{self.item_0!r}, {self.item_1!r}, {self.item_2!r}, "
            f"{self.item_3!r}, {self.item_4!r}, {self.item_5!r}, {self.item_6!r}], "
            f"kills={self.kills!r}, lane={self.lane!r}, perk_0={self.perk_0!r}, "
            f"perk_1={self.perk_1!r}, puuid={self.puuid!r}, "
            f"riot_id_game_name={self.riot_id_game_name!r}, "
            f"riot_id_tag_line={self.riot_id_tag_line!r}, "
            f"summoner_1_id={self.summoner_1_id!r}, summoner_2_id={self.summoner_2_id!r}, "
            f"summoner_id={self.summoner_id!r}, team_id={self.team_id!r}, "
            f"team_position={self.team_position!r}, "
            f"total_damage_dealt_to_champions={self.total_damage_dealt_to_champions!r}, "
            f"total_minions_killed={self.total_minions_killed!r}, "
            f"vision_score={self.vision_score!r}, "
            f"wards_placed={self.wards_placed!r}, win={self.win!r})"
        )
