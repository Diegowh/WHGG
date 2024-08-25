'''
Este módulo contiene varias DTOs que extienden de `pydantic.BaseModel`, responsables de
manejar los datos relacionados con `models.Account`.
'''
from typing import Optional

from pydantic import BaseModel

from backend.database.schemas.champion_stats import ChampionStats
from backend.database.schemas.league_entry import LeagueEntry
from backend.database.schemas.match import Match



class AccountBase(BaseModel):
    """Clase base para representar los datos de la cuenta de un usuario.
    """
    puuid: str
    summoner_id: str
    account_id: str
    game_name: str
    tag_line: str
    profile_icon_id: int
    summoner_level: int
    last_update: Optional[int] = None


class AccountCreate(AccountBase):
    """DTO para representar los datos necesarios para crear una nueva instancia
    de `models.Account`
    """

class AccountUpdate(BaseModel):
    """DTO para representar los datos necesarios para actualizar una instancia de
    `models.Account`
    """

    puuid: Optional[str] = None
    summoner_id: Optional[str] = None
    account_id: Optional[str] = None
    game_name: Optional[str] = None
    tag_line: Optional[str] = None
    profile_icon_id: Optional[int] = None
    summoner_level: Optional[int] = None
    last_update: Optional[int] = None


class Account(AccountBase):
    """DTO para representar una cuenta de un usuario.
    
    Se utiliza para transportar los datos obtenidos de una instancia de
    `models.Account`
    """

    id: int
    league_entries: Optional[list["LeagueEntry"]] = None
    matches: Optional[list["Match"]] = None
    champion_stats: Optional[list["ChampionStats"]] = None

    model_config = {
        "from_attributes": True
    }


class Response(Account):
    """DTO para representar los datos de una respuesta a 
    una petición `schemas.Request`
    """
