from typing import Optional
from pydantic import BaseModel

class ParticipantBase(BaseModel):
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
    participant_id: int
    perk_0: int
    perk_1: int
    puuid: str
    riot_id_game_name: str
    riot_id_tagline: str
    summoner_1_id: int
    summoner_2_id: int
    summoner_id: str
    team_id: int
    team_position: str
    total_damage_dealt_to_champions: int
    total_minions_killed: int
    vision_score: int
    wards_placed: int
    win: bool

class ParticipantCreate(ParticipantBase):
    pass


class Participant(ParticipantBase):
    id: int
    match_id: int

    class Config:
        orm_mode = True
