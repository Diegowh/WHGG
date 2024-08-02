from dataclasses import dataclass
from src.models.match.ban import Ban
from src.models.match.objectives import Objectives

@dataclass
class Team:
    bans: list[Ban]
    objectives: Objectives
    teamId: int
    win: bool
