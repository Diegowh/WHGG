"""
Gestiona la interacción entre los datos obtenidos de la API de RiotGames y la base de datos del backend.
El propósito principal del DataManager es centralizar la lógica de negocio relacionada con la obtención y persistencia de datos.
"""

import time
from typing import TYPE_CHECKING

from sqlalchemy.orm import Session

import backend.database.schemas as schemas
from backend.api.v1.schemas import Request, Response
from backend.core.riot_querier import RiotQuerier
from backend.database import crud
from backend.database.models import account
from backend.database.schemas.match import MatchCreate

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
    
    def _get_all_match_ids(self) -> list[str]:
        
        # Obtengo la lista de todos los match_ids desde el
        # comienzo de la season actual
        all_match_ids = []
        start = 0
        count = 100  # Limitado por la API de RiotGames
        
        while True:
            match_ids = self.querier.get_matches_by_puuid(
                puuid=self._puuid,
                region=self._region,
                start_time=self._season_start,
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
    
    
    def _fetch_match_and_participants(self, match_id) -> tuple[schemas.MatchCreate, list[schemas.ParticipantCreate]]:
        match_response = self.querier.get_match_by_match_id(
            match_id=match_id, 
            region=self._region
        )
        if match_response:
            match_data = match_response.get("info")
            participants_data: list = match_data.get("participants")
            
            participants =[]
            for participant in participants_data:
                if self._puuid == participant.get("puuid"):
                    player_data = participant
                
                participants.append(self._create_participant(participant))
            perk0 = player_data["perks"]["styles"][0]["selections"][0]["perk"]
            perk1 = player_data["perks"]["styles"][1]["style"]
            
            match = MatchCreate(
                match_id=match_id,
                game_creation=match_data.get("gameCreation"),
                game_duration=match_data.get("gameDuration"),
                game_end_timestamp=match_data.get("gameEndTimestamp"),
                game_mode=match_data.get("gameMode"),
                game_start_timestamp=match_data.get("gameStartTimestamp"),
                game_type=match_data.get("gameType"),
                game_version=match_data.get("gameVersion"),
                queue_id=match_data.get("queueId"),
                
                assists=player_data.get("assists"),
                champ_level=player_data.get("champLevel"),
                champion_id=player_data.get("championId"),
                champion_name=player_data.get("championName"),
                deaths=player_data.get("deaths"),
                gold_earned=player_data.get("goldEarned"),
                individual_position=player_data.get("individualPosition"),
                item_0=player_data.get("item0"),
                item_1=player_data.get("item1"),
                item_2=player_data.get("item2"),
                item_3=player_data.get("item3"),
                item_4=player_data.get("item4"),
                item_5=player_data.get("item5"),
                item_6=player_data.get("item6"),
                kills=player_data.get("kills"),
                lane=player_data.get("lane"),
                perk_0=perk0,
                perk_1=perk1,
                riot_id_game_name=player_data.get("riotIdGameName"),
                riot_id_tag_line=player_data.get("riotIdTagLine"),
                summoner_1_id=player_data.get("summoner1Id"),
                summoner_2_id=player_data.get("summoner2Id"),
                summoner_id=player_data.get("summonerId"),
                team_id=player_data.get("teamId"),
                team_position=player_data.get("teamPosition"),
                total_damage_dealt_to_champions=player_data.get("totalDamageDealtToChampions"),
                total_minions_killed=player_data.get("totalMinionsKilled"),
                vision_score=player_data.get("visionScore"),
                wards_placed=player_data.get("wardsPlaced"),
                win=player_data.get("win"),
            )
            return (match, participants)
    
    def _create_participant(self, participant_data: dict) -> schemas.ParticipantCreate:
        return schemas.ParticipantCreate(
            champion_id=participant_data.get("championId"),
            champion_name=participant_data.get("championName"),
            riot_id_game_name=participant_data.get("riotIdGameName"),
            riot_id_tagline=participant_data.get("riotIdTagLine"),
            team_id=participant_data.get("teamId"),
            team_position=participant_data.get("teamPosition")
        )
        
