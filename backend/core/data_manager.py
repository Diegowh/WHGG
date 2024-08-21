"""
Gestiona la interacción entre los datos obtenidos de la API de RiotGames y la base de datos del backend.
El propósito principal del DataManager es centralizar la lógica de negocio relacionada con la obtención y persistencia de datos.
"""

import time

from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound, IntegrityError
import backend.database.schemas as schemas
from backend.core.riot_querier import RiotQuerier
from backend.database import crud, models
from backend.database.schemas.match import MatchCreate




class DataManager:
    def __init__(self) -> None:
        self.querier = RiotQuerier()
        self._game_name = None
        self._tag_line = None
        self._region = None
        self._platform = None
        self._summoner_id: str = None
        self._puuid: str = None
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
    
    def set_summoner_id(self, summoner_id) -> None:
        self._summoner_id = summoner_id
        
    def set_puuid(self, puuid) -> None:
        self._puuid = puuid
        
    def get(self, request: schemas.Request, db: Session) -> schemas.Response:
        
        self.set_game_name(request.riot_id.game_name)
        self.set_tag_line(request.riot_id.tag_line)
        self.set_region(request.server.region)
        self.set_platform(request.server.platform)
        self.set_db(db)
        
        with self._db.begin(nested=True):
            # Compruebo si existe ese account en base de datos
            account_instance = self._get_or_create_account_model()
            
            # Compruebo si he de actualizar o no los datos del account
            # Si esta recien creado, y no tiene las entradas de League Entry, Match o ChampionStats
            # el last_update sera None
            now = int(time.time())
            if (account_instance.last_update is not None and (now - account_instance.last_update) <= 3600):
                return self._get_response(db_obj=account_instance)
            
            
            self._create_or_update_league_entries (account_instance)
            
            # En base a los datos de cada match, crea las entradas para Match, Participant
            # Y crea o actualiza los ChampionStats
            self._create_matches(account_instance)
            
            # Una vez termina de crear todas las entradas a las tablas relacionadas con Account
            # es cuando se asigna el last_update
            now = int(time.time())
            account_instance = crud.update_account_last_update(
                db=self._db, 
                db_obj=account_instance,
                last_update=now
                )

            return self._get_response(db_obj=account_instance)
        
    def _get_response(self, db_obj: models.Account) -> schemas.Response:
        response = crud.get_response(db=self._db, db_obj=db_obj)
        return schemas.Response.model_validate(response)
    
    
    def _fetch_account(self) -> schemas.AccountCreate:
        
        account_response = self.querier.get_account_by_riot_id(
            game_name=self._game_name, 
            tag_line=self._tag_line, 
            region=self._region
            )
        if account_response is not None:
            puuid = account_response.get("puuid")

            summoner_response = self.querier.get_summoner_by_puuid(
                puuid=puuid,
                platform=self._platform
            )
            summoner_id = summoner_response.get("id")
            account_id = summoner_response.get("accountId")
            profile_icon_id = summoner_response.get("profileIconId")
            summoner_level = summoner_response.get("summonerLevel")
            
            return schemas.AccountCreate(
                puuid=puuid,
                summoner_id=summoner_id,
                account_id=account_id,
                game_name=self._game_name,
                tag_line=self._tag_line,
                profile_icon_id=profile_icon_id,
                summoner_level=summoner_level,
            )
        return None
            
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
            
            participants = []
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
    
    def _create_match_entries(self, acc_instance: models.Account):
        matches_in_db: int = crud.count_matches(
            db=self._db,
            db_obj=acc_instance
        )
        match_ids = self._get_match_ids(start_index=matches_in_db)
        for match_id in match_ids:
            match, participants = self._fetch_match_and_participants(match_id)
            match = crud.create_match(
                db=self._db,
                account=acc_instance,
                match=match
            )
            
            self._create_or_update_champion_stats(match)
            
            for participant in participants:
                crud.create_participant(
                    db=self._db,
                    participant=participant,
                    match_id=match.id
                )
        
        
    def _create_participant(self, participant_data: dict) -> schemas.ParticipantCreate:
        return schemas.ParticipantCreate(
            champion_id=participant_data.get("championId"),
            champion_name=participant_data.get("championName"),
            riot_id_game_name=participant_data.get("riotIdGameName"),
            riot_id_tagline=participant_data.get("riotIdTagline"),
            team_id=participant_data.get("teamId"),
            team_position=participant_data.get("teamPosition")
        )
        
        
    def _create_or_update_champion_stats(self, match: models.Match):
        try:
            cs_instance = crud.get_champion_stats(
                self._db,
                account_id=match.account_id,
                name=match.champion_name
            )
            
            games_played = cs_instance.games_played + 1
            k_avg = self._calculate_avg(
                match.kills, cs_instance.kill_avg, games_played
            )
            d_avg = self._calculate_avg(
                match.deaths, cs_instance.death_avg, games_played
            )
            a_avg = self._calculate_avg(
                match.assists, cs_instance.assist_avg, games_played
            )
            new_kda = self._calculate_kda(
                k_avg, d_avg, a_avg
            )
            new_wins = cs_instance + 1 if match.win else None
            new_losses = cs_instance + 1 if not match.win else None
            new_wr = self._calculate_winrate(new_wins, new_losses)
            champion_stats_update = schemas.ChampionStatsUpdate(
                games_played=cs_instance.games_played + 1,
                kill_avg=k_avg,
                death_avg=d_avg,
                assist_avg=a_avg,
                kda=new_kda,
                wins=new_wins,
                losses=new_losses,
                winrate=new_wr,
            )
            
            crud.update_champion_stats(
                db=self._db,
                id=cs_instance.id,
                champion_stats=champion_stats_update
            )
            
        except NoResultFound:
            # Creo la primera entrada ChampionStats
            # para ese Account.id y champion_name
            new_cs_instance = crud.create_champion_stats(
                db=self._db,
                account_id=match.account_id,
                champion_stats=schemas.ChampionStatsCreate(
                    name=match.champion_name,
                    kill_avg=match.kills,
                    death_avg=match.deaths,
                    assists_avg=match.kills,
                    kda=self._calculate_kda(match.kills, match.deaths, match.assists),
                    winrate=self._calculate_winrate(match.wins, 1),
                    games_played=1,
                    wins= 1 if match.win else 0,
                    losses=1 if not match.win else 1,
                )
            )

    def _get_or_create_account_model(self) -> models.Account:
        account_model = crud.get_account_by_game_name_and_tag_line(
            db=self._db,
            game_name=self._game_name,
            tag_line=self._tag_line
        )
        if account_model is None:
            new_account_data = self._fetch_account()
            self.set_summoner_id(new_account_data.summoner_id)
            self.set_puuid(new_account_data.puuid)
            account_model = crud.create_account(db=self._db, account=new_account_data) 
        
        return account_model


    def _create_or_update_league_entries(self, db_obj: models.Account):
        league_entries = self._fetch_league_entries()
        for league_entry in league_entries:
            existing_entry = crud.get_league_entry_by_queue_type(
                db=self._db,
                account_id=db_obj.id,
                queue_type=league_entry.queue_type
            )
            
            if existing_entry:
                update_data = schemas.LeagueEntryUpdate(
                    tier=league_entry.tier,
                    rank=league_entry.rank,
                    league_points=league_entry.league_points,
                    wins=league_entry.wins,
                    losses=league_entry.losses
                )
                crud.update_league_entry(
                    db=self._db,
                    db_obj=existing_entry,
                    obj_in=update_data
                )
            
            else:
                try:
                    crud.create_league_entry(
                        db=self._db,
                        league_entry=league_entry,
                        account_id=db_obj.id
                    )
                except IntegrityError:
                    self._db.rollback()
                    print("Error inesperado al crear la entrada LeagueEntry")
    
    def _create_matches(self, db_obj: models.Account):
        matches_in_db: int = crud.count_matches(
            db=self._db,
            db_obj=db_obj
        )
        match_ids = self._get_match_ids(start_index=matches_in_db)
        for match_id in match_ids:
            match, participants = self._fetch_match_and_participants(match_id)
            match = crud.create_match(
                db=self._db,
                match=match,
                account_id=db_obj.id
            )
            
            self._create_or_update_champion_stats(match)
            
            for participant in participants:
                crud.create_participant(
                    db=self._db,
                    participant=participant,
                    match_id=match.id
                )
    
    def _calculate_kda(self, k: float, d: float, a: float) -> float:
        if d == 0:
            d = 1  # Para evitar division por 0
        return round(((k + a) / d), 2)
    
    def _calculate_winrate(self, wins: int, games: int) -> int:
        return int((wins / games) * 100)
    
    def _calculate_avg(self, unit: int, prev_avg: int, games_played: int) -> float:
        prev_unit = prev_avg * (games_played - 1)
        total_unit = prev_unit + unit
        return round((total_unit / games_played), 2)