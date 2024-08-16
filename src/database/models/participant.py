from sqlalchemy import ForeignKey
from src.database.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.database.models.match import Match
    

class Participant(Base):
    __tablename__ = "participant"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    match_id: Mapped[int] = mapped_column(ForeignKey("match.id"))
    match: Mapped["Match"] = relationship(back_populates="participants")


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
    # Lo comento porque creo que usare solo totalMinionsKilled
    # neutralMinionsKilled: Mapped[int]  
    participant_id: Mapped[int]
    # https://ddragon.leagueoflegends.com/cdn/14.15.1/data/en_US/runesReforged.json
    perk_0: Mapped[int]  # Runa Principal
    perk_1: Mapped[int]  # Runa Secundaria
    puuid: Mapped[str]
    riot_id_game_name: Mapped[str]
    riot_id_tagline: Mapped[str]
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
