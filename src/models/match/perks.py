from dataclasses import dataclass
from src.models.match.perk_stats import PerkStats
from src.models.match.perk_style import PerkStyle

@dataclass
class Perks:
    statPerks: PerkStats
    styles: list[PerkStyle]