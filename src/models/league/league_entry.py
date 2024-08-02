from __future__ import annotations
from src.models.account.account import Account
from dataclasses import dataclass


@dataclass
class LeagueEntry:
    leagueId: str
    queueType: str
    tier: str
    rank: str
    summonerId: Account.summoner_id
    leaguePoints: int
    wins: int
    losses: int
    veteran: bool
    inactive: bool
    freshBlood: bool
    hotStreak: bool