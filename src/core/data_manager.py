"""
Transforma y filtra los datos crudos de la API de Riot en los modelos de database/schemas
"""

import time
from typing import TYPE_CHECKING


from src.core.riot_querier import RiotQuerier
import src.database.schemas as schemas
from src.schemas import RequestDto, ResponseDto

if TYPE_CHECKING:
    from src.config import Settings



class DataManager:
    def __init__(self, request: RequestDto, settings: 'Settings') -> None:
        self.querier = RiotQuerier(settings)
        self._game_name = request.riot_id.game_name
        self._tag_line = request.riot_id.tag_line
        self._region = request.server.region
        self._platform = request.server.platform
        self._summoner_id = None
        self._puuid = None
        self._settings = settings

    def get(request) -> ResponseDto:
        """
        Comprueba la cache
        Si existen en cache
        Los retorna
        Si no existen en cache
        Comprueba si existen en base de datos
        Si existen en la base de datos
        Comprueba la fecha de la ultima actualizacion de estos
        Si ha pasado menos tiempo del 'treshold'
        Los retorna
        Si ha pasado mas tiempo del 'treshold'
        Los obtiene de la API de Riot y los actualiza en la DB
        Los retorna
        Si no existen en la base de datos
        Los obtiene de la API de Riot y los crea en la DB
        Los Retorna
        """
    
    def _fetch_account(self) -> schemas.AccountCreate:
        
        account_response = self.querier.get_account_by_riot_id(
            game_name=self._game_name, 
            tag_line=self._tag_line, 
            region=self._region
            )
        if account_response is not None:
            self._puuid = account_response.get("puuid")

            summoner_response = self.querier.get_summoner_by_puuid(
                puuid=self._puuid,
                platform=self._platform
            )
            self._summoner_id = summoner_response.get("id")
            account_id = summoner_response.get("accountId")
            profile_icon_id = summoner_response.get("profileIconId")
            summoner_level = summoner_response.get("summonerLevel")
            last_update = int(time.time())
            
            return schemas.AccountCreate(
                puuid=self._puuid,
                summoner_id=self._summoner_id,
                account_id=account_id,
                game_name=self._game_name,
                tag_line=self._tag_line,
                profile_icon_id=profile_icon_id,
                summoner_level=summoner_level,
                last_update=last_update
            )
            
    def _fetch_league_entries(self) -> list[schemas.LeagueEntryCreate]:
        league_entries = []
        if self._summoner_id is not None:
            league_entries_response = self.querier.get_league_entries_by_summoner_id(
                summoner_id=self._summoner_id,
                platform=self._platform
            )
            
            for entry in league_entries_response:
                league_entry = schemas.LeagueEntryCreate(
                    queue_type=entry.get("queueType"),
                    tier=entry.get("tier"),
                    rank=entry.get("rank"),
                    league_points=entry.get("leaguePoints"),
                    wins=entry.get("wins"),
                    losses=entry.get("losses")
                )
                league_entries.append(league_entry)
            
        return league_entries
    
    def _get_all_match_ids(self, season_start: int) -> list[str]:
        
        # Obtengo la lista de todos los match_ids desde el
        # comienzo de la season actual
        all_match_ids = []
        start = 0
        count = 100  # Limitado por la API de RiotGames
        
        while True:
            match_ids = self.querier.get_matches_by_puuid(
                puuid=self._puuid,
                region=self._region,
                start_time=season_start,
                start=start,
                count=count
            )
            if not match_ids:
                break
            
            all_match_ids.extend(match_ids)
            
            if len(match_ids) < count:
                # Si recibimos menos de 100 partidas, significa que
                # no recibiremos mas si realizamos una consulta extra
                break
            
            start += count
        
        return all_match_ids