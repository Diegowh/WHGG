from __future__ import annotations
from dataclasses import dataclass
from src.models.match.participant import Participant
from src.models.match.team import Team


@dataclass
class Info:
    endOfGameResult: str
    gameCreation: int
    gameDuration: int
    gameEndTimestamp: int
    gameId: int
    gameMode: str
    gameName: str
    gameStartTimestamp: int
    gameType: str
    gameVersion: str
    mapId: int
    participants: list[Participant]
    platformId: str
    queueId: int
    teams: list[Team]
    tournamentCode: str
