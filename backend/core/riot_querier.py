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

import time

import httpx

from backend.config import settings
from backend.core.ratelimiter.rate_limiter import RateLimitedClient
from backend.core.exceptions import DataNotFoundError


class RiotQuerier:
    """Se encarga de realizar las llamadas a la API de Riot Games y manejar la autenticación
    """

    def __init__(self) -> None:

        self._base_url = "https://{server}.api.riotgames.com"

        self._endpoints = {

            # Region
            "account": "/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}",
            "match": "/lol/match/v5/matches/{match_id}",
            "matches": "/lol/match/v5/matches/by-puuid/{puuid}/ids",

            # Platform
            "summoner": "/lol/summoner/v4/summoners/by-puuid/{puuid}",
            "league_entry": "/lol/league/v4/entries/by-summoner/{summoner_id}",
        }

        self._client = RateLimitedClient(
            interval=1.2,
            headers={"X-Riot-Token": settings.RIOT_API_KEY}
        )

    def _fetch(
        self,
        url: str,
        params: dict | None = None,
        retry: bool = True
    ):
        try:
            response = self._client.get(url, params=params)

            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:  # Rate limit
                retry_after = e.response.headers.get('Retry-After')
                if retry_after:
                    time_to_wait = int(retry_after)
                else:
                    time_to_wait = 10  # Tiempo default si no existe el Retry-After

                print(f"Rate limit exceeded. Retrying in {time_to_wait} seconds...")
                time.sleep(time_to_wait)

                if retry:
                    return self._fetch(url, params, retry)  # Reintento
                return None

            if e.response.status_code == 404:
                raise DataNotFoundError("Data not found") from e

            print(f"HTTP Error occurred: {e.response.status_code} - {e.response.text}")
            return None

    def get_account_by_riot_id(self, game_name: str, tag_line: str, region: str) -> dict:
        """
        Retorna el resultado de: 
        https://developer.riotgames.com/apis#account-v1/GET_getByRiotId
        """
        url = (self._base_url + self._endpoints.get("account")).format(
            server=region,
            game_name=game_name,
            tag_line=tag_line
        )
        return self._fetch(url)

    def get_summoner_by_puuid(self, puuid: str, platform: str) -> dict:
        """
        Retorna el resultado de: 
        https://developer.riotgames.com/apis#summoner-v4/GET_getByPUUID
        """
        url = (self._base_url + self._endpoints.get("summoner")).format(
            server=platform,
            puuid=puuid
        )
        return self._fetch(url)

    def get_matches_by_puuid(  # pylint: disable=too-many-arguments
            self,
            puuid: str,
            region: str,
            start_time: int = None,
            end_time: int = None,
            queue: int = None,
            type: str = None,  # pylint: disable=redefined-builtin
            start: int = 0,
            count: int = 20
    ) -> list[str]:
        """
        Retorna el resultado de:
        https://developer.riotgames.com/apis#match-v5/GET_getMatchIdsByPUUID
        """
        # Crea los parametros filtrando los que sean nulos
        params = {k: v for k, v in {
            "startTime": start_time,
            "endTime": end_time,
            "queue": queue,
            "type": type,
            "start": start,
            "count": count
        }.items() if v is not None}

        url = (self._base_url + self._endpoints.get("matches")).format(
            server=region,
            puuid=puuid
        )

        return self._fetch(url, params=params)

    def get_match_by_match_id(self, match_id: str, region: str) -> dict:
        """
        Retorna el resultado de:
        https://developer.riotgames.com/apis#match-v5/GET_getMatch
        """
        url = (self._base_url + self._endpoints.get("match")).format(
            server=region,
            match_id=match_id
        )
        return self._fetch(url)

    def get_league_entries_by_summoner_id(self, summoner_id: str, platform: str) -> list[dict]:
        """
        Retorna el resultado de:
        https://developer.riotgames.com/apis#league-v4/GET_getLeagueEntriesForSummoner
        """
        url = (self._base_url + self._endpoints.get("league_entry")).format(
            server=platform,
            summoner_id=summoner_id
        )
        return self._fetch(url)
