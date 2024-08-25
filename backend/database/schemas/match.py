'''
Este módulo contiene varias DTOs que extienden de `pydantic.BaseModel`, responsables de
manejar los datos relacionados con `models.Match`.
'''
from pydantic import BaseModel

from backend.database.schemas.participant import Participant



class MatchBase(BaseModel):
    """Clase base para representar la información de una partida jugada por un usuario"""

    match_id: str
    game_creation: int
    game_duration: int
    game_end_timestamp: int
    game_mode: str
    game_start_timestamp: int
    game_type: str
    game_version: str
    queue_id: int

    assists: int
    champ_level: int
    champion_id: int
    champion_name: str
    deaths: int
    gold_earned: int
    individual_position: str
    item_0: int
    item_1: int
    item_2: int
    item_3: int
    item_4: int
    item_5: int
    item_6: int
    kills: int
    lane: str
    # https://ddragon.leagueoflegends.com/cdn/14.15.1/data/en_US/runesReforged.json
    perk_0: int  # Runa Principal
    perk_1: int  # Runa Secundaria
    puuid: str
    riot_id_game_name: str
    riot_id_tag_line: str
    summoner_1_id: int
    summoner_2_id: int
    summoner_id: str
    team_id: int
    team_position: str
    total_damage_dealt_to_champions: int
    total_minions_killed: int  # Suma neutralMinionsKilled + totalMinionsKilled
    vision_score: int
    wards_placed: int
    win: bool

class MatchCreate(MatchBase):
    """DTO para representar los datos necesarios para crear una nueva instancia de
    `models.Match`
    """


class Match(MatchBase):
    """DTO para representar una partida jugada por un usuario
    
    Se utiliza para transportar los datos obtenidos de una instancia de
    `models.Match`
    """

    id: int
    account_id: int
    participants: list["Participant"] = []

    model_config = {
        "from_attributes": True
    }
