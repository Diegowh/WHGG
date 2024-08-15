'''
Este modulo se encarga de realizar las llamadas a la API de RiotGames y manejar la autenticación,
el rate limiting y el procesamiento de los datos recibidos.
https://developer.riotgames.com/apis
Requiere de tener configurada una API Key válida en un archivo .env

Hace peticiones a los siguientes endpoints:
      # Region 
    - https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/
    - https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/
    - https://europe.api.riotgames.com/lol/match/v5/matches/
    
      # Platform
    - https://euw1.api.riotgames.com/lol/summoner/v4/summoners/
    - https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/
'''

from typing import TYPE_CHECKING, Optional

import httpx
if TYPE_CHECKING:
    from src.schemas.riot_server import RiotServer
    from src.config import Settings


class RiotQuerier:
    
    def __init__(self, server: 'RiotServer', settings: 'Settings') -> None:
        
        self._server = server.name
        self._region = server.region
        self._platform = server.platform
        self._base_url = "https://{server}.api.riotgames.com"

        # Region
        self._account_endpoint = "/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"  
        self._match_endpoint = "/lol/match/v5/matches/{match_id}"
        self._matches_endpoint = "/lol/match/v5/matches/by-puuid/{puuid}/ids"

        # Platform
        self._summoner_endpoint = "/lol/summoner/v4/summoners/by-puuid/{puuid}"  
        self._league_entry_endpoint = "/lol/league/v4/entries/by-summoner/{summoner_id}"  
        self._client = httpx.AsyncClient(headers={"X-Riot-Token": settings.RIOT_API_KEY})
    
    async def _fetch(self, endpoint: str, method: str = 'GET', params: Optional[dict] = None, data: Optional[dict] = None, **kwargs):
        url = (self._base_url + endpoint).format(
            server=self.set_server(endpoint),
            **kwargs
        )

        try:
            if method == 'GET':
                response = await self._client.get(url, params=params)
            else:
                response = await self._client.request(method=method, url=url, json=data)

            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            print(f"HTTP Error occurred: {e.response.status_code} - {e.response.text}")
            return None


    def set_server(self, endpoint: str) -> str:
        """
        Asigna un servidor válido en base al endpoint.
        Algunos endpoints requieren como servidor una 'platform' y otros una 'region'.

        Region se refiere a "Europe", "America", etc.
        Platform se refire a "euw1", "na1", etc.
        """
        if endpoint == self._account_endpoint or endpoint == self._match_endpoint or endpoint == self._matches_endpoint:
            return self._region
        return self._platform
    

    async def get_account_by_riot_id(self, game_name: str, tag_line: str) -> dict:
        """Retorna el resultado de: https://developer.riotgames.com/apis#account-v1/GET_getByRiotId"""
        return await self._fetch(
            endpoint=self._account_endpoint, 
            game_name=game_name, 
            tag_line=tag_line
        )

    async def get_summoner_by_puuid(self, puuid: str) -> dict:
        """Retorna el resultado de: https://developer.riotgames.com/apis#summoner-v4/GET_getByPUUID"""
        return await self._fetch(
            endpoint=self._summoner_endpoint,
            puuid=puuid
        )
    
    async def get_matches_by_puuid(self, puuid: str, start_time: int = None, end_time: int = None, queue: int = None, type: str = None, start: int = 0, count: int = 20) -> list[str]:
        """Retorna el resultado de: https://developer.riotgames.com/apis#match-v5/GET_getMatchIdsByPUUID"""

        # Crea los parametros filtrando los que sean nulos
        params = {k: v for k, v in {
            "startTime": start_time,
            "endTime": end_time,
            "queue": queue,
            "type": type,
            "start": start,
            "count": count
        }.items() if v is not None}


        return await self._fetch(
            endpoint=self._matches_endpoint,
            puuid=puuid,
            params=params
        )
    
    async def get_match_by_match_id(self, match_id: str) -> dict:
        """Retorna el resultado de: https://developer.riotgames.com/apis#match-v5/GET_getMatch"""

        return await self._fetch(
            endpoint=self._match_endpoint, 
            match_id=match_id
        )

    async def get_league_entry_by_summoner_id(self, summoner_id: str) -> list[dict]:
        """Retorna el resultado de: https://developer.riotgames.com/apis#league-v4/GET_getLeagueEntriesForSummoner"""

        return await self._fetch(
            endpoint=self._league_entry_endpoint,
            summoner_id=summoner_id
        )
