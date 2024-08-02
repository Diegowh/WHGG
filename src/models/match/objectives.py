from dataclasses import dataclass
from src.models.match.objective import Objective


@dataclass
class Objectives:
    baron: Objective
    champion: Objective
    dragon: Objective
    horde: Objective
    inhibitor: Objective
    riftHerald: Objective
    tower: Objective
