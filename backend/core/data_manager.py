"""
Gestiona la interacción entre los datos obtenidos de la API de RiotGames y la base de datos del backend.
El propósito principal del DataManager es centralizar la lógica de negocio relacionada con la obtención y persistencia de datos.
"""

import time
from typing import TYPE_CHECKING

from sqlalchemy.orm import Session

import backend.database.schemas as schemas
from backend.core.riot_querier import RiotQuerier
from backend.database import crud
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
        
        
    def get(self, request: schemas.Request, db: Session) -> schemas.Response:
        
        self.set_game_name(request.riot_id.game_name)
        self.set_tag_line(request.riot_id.tag_line)
        self.set_region(request.server.region)
        self.set_platform(request.server.platform)
        self.set_db(db)
        
        # Compruebo si existe ese account en base de datos
        account_model = crud.get_account_by_game_name_and_tag_line(
            db=self._db,
            game_name=self._game_name,
            tag_line=self._tag_line
        )
        if account_model is not None:
            
            # Compruebo el tiempo transcurrido desde la ultima actualizacion/peticion
            time_now = int(time.time())
            if time_now - account_model.last_update <= 3600:  # 3600 segundos / 1 hora
                account = schemas.Account.model_validate(account_model)
                return schemas.Response(**account.model_dump())

            # Ha pasado mas de 1 hora desde la ultima vez que se solicitaron
            # Los solicito a la API de RiotGames
            new_account_data = self._fetch_account()
            new_account_data = schemas.AccountUpdate(**new_account_data.model_dump())
            # Actualizo los datos
            updated_acc = crud.update_account(
                db=self._db,
                account=new_account_data
            )
            
            new_league_entries = self._fetch_league_entries()
            for league_entry in new_league_entries:
                # No sabemos si existen league entries previas para las queue_type actuales
                # Por lo tanto comprobamos primero cuales son las queue_type de las 
                # league entry existentes para saber si actualizar o crear
                league_entry_exist = crud.get_league_entry_by_queue_type(
                    db=self._db,
                    account_id=account_model.id,
                    queue_type=league_entry.queue_type
                )
                if league_entry_exist:
                    new_league_entry_data = schemas.LeagueEntryUpdate(**league_entry.model_dump())
                    crud.update_league_entry(
                        db=self._db,
                        id=league_entry_exist.id,
                        league_entry=new_league_entry_data
                    )
                else:
                    crud.create_league_entry(
                        db=self._db,
                        league_entry=league_entry,
                        account_id=account_model.id
                    )

            # Necesito saber cual es el match mas reciente que existe en la base de datos
            # Para solicitar unicamente los jugados a partir de ese
            matches_in_db = crud.count_matches(
                db=self._db,
                account_id=account_model.id
            )
            new_match_ids = self._get_match_ids(matches_in_db)
            for match_id in new_match_ids:
                new_match, new_participants = self._fetch_match_and_participants(match_id)
                match = crud.create_match(
                    db=self._db,
                    match=new_match,
                    account_id=account_model.id
                )
                for participant in new_participants:
                    crud.create_participant(
                        db=self._db,
                        participant=participant,
                        match_id=match.id
                    )

            
        updated_account_model = crud.get_account_by_game_name_and_tag_line(
        db=self._db,
        game_name=self._game_name,
        tag_line=self._tag_line
        )
        return schemas.Response.model_validate(updated_account_model)
            

        """
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
    
    def _get_match_ids(self, start_index: int = 0) -> list[str]:
        
        # Obtengo la lista de todos los match_ids desde el
        # comienzo de la season actual
        all_match_ids = []
        start = start_index
        count = 100 # Limitado por la API de RiotGames
        
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
