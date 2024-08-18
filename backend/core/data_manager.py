"""
Gestiona la interacción entre los datos obtenidos de la API de RiotGames y la base de datos del backend.
El propósito principal del DataManager es centralizar la lógica de negocio relacionada con la obtención y persistencia de datos.
"""

import time
from typing import TYPE_CHECKING


from backend.core.riot_querier import RiotQuerier
from backend.database import crud
from backend.database.models import account
import backend.database.schemas as schemas
from backend.api.v1.schemas import Request, Response
from backend.database.schemas.match import MatchCreate
from sqlalchemy.orm import Session
if TYPE_CHECKING:
    from backend.config import Settings



class DataManager:
    def __init__(self, settings: 'Settings') -> None:
        self.querier = RiotQuerier(settings)
        self._game_name = None
        self._tag_line = None
        self._region = None
        self._platform = None
        self._summoner_id: str = None
        self._puuid: str = None
        self._settings = settings
        self._db = None
        self._season_start: int = None


    def set_game_name(self, game_name) -> None:
        self._game_name = game_name
        
    def set_tag_line(self, tag_line) -> None:
        self._tag_line = tag_line
        
    def set_region(self, region) -> None:
        self._region = region
    
    def set_platform(self, platform) -> None:
        self._platform = platform
        
    def set_db(self, db: Session) -> None:
        self._db = db
        
        
