'''
Este módulo contiene varias DTOs que extienden de `pydantic.BaseModel`, responsables de
manejar los datos relacionados con `models.LeagueEntry`.
'''
from typing import Optional

from pydantic import BaseModel


class LeagueEntryBase(BaseModel):
    """Clase base para representar la información de una cola de clasificatoria
    de un usuario"""

    queue_type: str
    tier: Optional[str] = None
    rank: Optional[str] = None
    league_points: int
    wins: int
    losses: int

class LeagueEntryCreate(LeagueEntryBase):
    """DTO para representar los datos necesarios para crear una nueva instancia de
    `models.LeagueEntry`
    """


class LeagueEntryUpdate(BaseModel):
    """DTO para representar los datos necesarios para actualizar una instancia de
    `models.LeagueEntry`
    """

    queue_type: Optional[str] = None
    tier: Optional[str] = None
    rank: Optional[str] = None
    league_points: Optional[int] = None
    wins: Optional[int] = None
    losses: Optional[int] = None


class LeagueEntry(LeagueEntryBase):
    """DTO para representar una cola de clasificatoria de un usuario.
    
    Se utiliza para transportar los datos obtenidos de una instancia
    de `models.LeagueEntry`
    """

    id: int
    account_id: int

    model_config = {
        "from_attributes": True
    }
