from typing import Optional

from pydantic import BaseModel


class ChampionStatsBase(BaseModel):
    name: str
    games_played: int
    kill_avg: float
    death_avg: float
    assist_avg: float
    kda: float
    wins: int
    losses: int
    winrate: int

class ChampionStatsCreate(ChampionStatsBase):
    pass

class ChampionStatsUpdate(BaseModel):
    name: Optional[str] = None
    games_played: Optional[int] = None
    kill_avg: Optional[float] = None
    death_avg: Optional[float] = None
    assist_avg: Optional[float] = None
    kda: Optional[float] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    winrate: Optional[int] = None

class ChampionStats(ChampionStatsBase):
    id: int
    account_id: int

    model_config = {
        "from_attributes": True
    }