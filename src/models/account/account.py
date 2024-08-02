from __future__ import annotations
from src.models.league.league_entry import LeagueEntry
from dataclasses import dataclass


@dataclass
class Account:
    summonerId: str
    accountId: str
    puuid: str
    gameName: str
    tagLine: str
    profileIconId: int
    revisionDate: int
    summonerLevel: int
    league: set[LeagueEntry]
    
