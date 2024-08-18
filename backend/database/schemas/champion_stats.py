from typing import Optional

from pydantic import BaseModel


class ChampionStatsBase(BaseModel):
    name: str
    kda: float
    kill_avg: float
    death_avg: float
    assist_avg: float
    winrate: int
    games_played: int

class ChampionStatsCreate(ChampionStatsBase):
    pass

class ChampionStatsUpdate(BaseModel):
    name: Optional[str] = None
    kda: Optional[float] = None
    kill_avg: Optional[float] = None
    death_avg: Optional[float] = None
    assist_avg: Optional[float] = None
    winrate: Optional[int] = None
    games_played: Optional[int] = None

class ChampionStats(ChampionStatsBase):
    id: int
    account_id: int

    class Config:
        orm_mode = True