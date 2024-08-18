from typing import Optional

from pydantic import BaseModel


class LeagueEntryBase(BaseModel):
    queue_type: str
    tier: str
    rank: str
    league_points: int
    wins: int
    losses: int

class LeagueEntryCreate(LeagueEntryBase):
    pass

class LeagueEntryUpdate(BaseModel):
    queue_type: Optional[str] = None
    tier: Optional[str] = None
    rank: Optional[str] = None
    league_points: Optional[int] = None
    wins: Optional[int] = None
    losses: Optional[int] = None

class LeagueEntry(LeagueEntryBase):
    id: int
    account_id: str

    class Config:
        orm_mode = True
