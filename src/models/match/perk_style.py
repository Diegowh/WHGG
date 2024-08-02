from dataclasses import dataclass
from src.models.match.perk_style_selection import PerkStyleSelection


@dataclass
class PerkStyle:
    description: str
    selections: list[PerkStyleSelection]
    style: int

    