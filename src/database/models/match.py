from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.database.models.account import Account
    from src.database.models.participant import Participant



class Match(Base):
    __tablename__ = "match"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    account: Mapped["Account"] = relationship(back_populates="matches")
    
    participants: Mapped[list["Participant"]] = relationship(back_populates="match", cascade="all, delete-orphan")

    match_id: Mapped[str]
    game_creation: Mapped[int]
    game_duration: Mapped[int]
    game_end_timestamp: Mapped[int]
    game_mode: Mapped[str]
    game_start_timestamp: Mapped[int]
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
        return (f"Match(id={self.id!r}, account_id={self.account_id!r}, "
                f"info_id={self.info_id!r})")