from typing import Optional
from pydantic import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.database.schemas.participant import Participant



class MatchBase(BaseModel):
    match_id: str
    game_creation: int
    game_duration: int
    game_end_timestamp: int
    game_mode: str
    game_start_timestamp: int
    game_type: str
    game_version: str
    queue_id: int

class MatchCreate(MatchBase):
    pass


class Match(MatchBase):
    id: int
    account_id: int
    participants: list["Participant"] = []

    class Config:
        orm_mode = True
