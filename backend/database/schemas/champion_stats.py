'''
Este módulo contiene varias DTOs que extienden de `pydantic.BaseModel`, responsables de
manejar los datos relacionados con `models.ChampionStats`.
'''
from typing import Optional

from pydantic import BaseModel


class ChampionStatsBase(BaseModel):
    """Clase base para representar los datos de un campeon de league of legends
    jugado por el usuario.
    """

    name: str
    games_played: int
    kill_avg: float
    death_avg: float
    assist_avg: float
    kda: float
    wins: int
    losses: int
    winrate: int

class ChampionStatsCreate(ChampionStatsBase):
    """DTO para representar los datos necesarios para crear una nueva instancia de
    `models.ChampionStats`
    """


class ChampionStatsUpdate(BaseModel):
    """DTO para representar los datos necesarios para actualizar una instancia de
    `models.ChampionStats`
    """

    name: Optional[str] = None
    games_played: Optional[int] = None
    kill_avg: Optional[float] = None
    death_avg: Optional[float] = None
    assist_avg: Optional[float] = None
    kda: Optional[float] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    winrate: Optional[int] = None


class ChampionStats(ChampionStatsBase):
    """DTO para representar los datos de un campeon de league of legends
    jugado por el usuario.
    
    Se utiliza para transportar los datos obtenidos de una instancia
    de `models.ChampionStats`
    """

    id: int
    account_id: int

    model_config = {
        "from_attributes": True
    }
