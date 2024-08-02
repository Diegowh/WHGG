from dataclasses import dataclass


@dataclass
class Ban:
    championId: int
    pickTurn: int
