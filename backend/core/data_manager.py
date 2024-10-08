'''
Módulo que proporciona un controlador para la gestión de datos del backend.

Este módulo centraliza la lógica de negocio para la obtención y persistencia de datos.
'''

import time

from sqlalchemy.orm import Session
from backend.core.exceptions import DataNotFoundError
from backend.database import schemas
from backend.core.riot_querier import RiotQuerier
from backend.database import crud, models
from backend.database.schemas.match import MatchCreate
from backend.config import settings
from backend.database.schemas.request import RiotId, RiotServer


class DataManager:
    """Controlador para la gestión de datos del backend.
    
    Maneja las solicitudes recibidas, interactuando con la base de datos
    para obtener, crear o actualizar información. 
    
    Utiliza un querier `RiotQuerier`
    para realizar solicitudes a la API de Riot Games.
    """
    def __init__(self) -> None:
        self.querier = RiotQuerier()

        self._riot_id: RiotId = None
        self._server: RiotServer = None

        self._summoner_id: str = None
        self._puuid: str = None
        self._db = None

    def set_riot_id(self, riot_id) -> None:
        """Asigna un nuevo valor a self._riot_id"""
        self._riot_id = riot_id

    def set_server(self, server) -> None:
        """Asigna un nuevo valor a self._server"""
        self._server = server

    def set_db(self, db: Session) -> None:
        """Asigna un nuevo valor a self._db"""
        self._db = db

    def set_summoner_id(self, summoner_id) -> None:
        """Asigna un nuevo valor a self._summoner_id"""
        self._summoner_id = summoner_id

    def set_puuid(self, puuid) -> None:
        """Asigna un nuevo valor a self._puuid"""
        self._puuid = puuid

    def get(
        self,
        request: schemas.Request,
        db: Session
    ) -> schemas.Response:
        """Obtiene los datos para una request.
        Maneja una solicitud para obtener los datos de una cuenta de
        League of Legends.
        
        Primero, verifica si la cuenta ya existe en la base de datos.
        Si la cuenta está presente y los datos se han actualizado previamente
        en el marco de tiempo establecido, devuelve la información almacenada
        en la base de datos.
        
        Si los datos no existen o están desactualizados, actualiza o crea entradas
        en la base de datos obteniendo los nuevos datos de la API de Riot Games.

        Args:
            request (schemas.Request): Objeto que contiene la información requerida
            para realizar la consulta.
            db (Session): Sesión de base de datos para realizar las operaciones
            necesarias.

        Returns:
            schemas.Response: Objeto que contiene la información actualizada de la
            cuenta.
        """
        self.set_riot_id(request.riot_id)
        self.set_server(request.server)
        self.set_db(db)

        with self._db.begin(nested=True):
            try:
                # Compruebo si existe ese account en base de datos
                account_instance = self._get_or_create_account_model()
            except DataNotFoundError:
                raise DataNotFoundError
    
            # Compruebo si he de actualizar o no los datos del account
            # Si esta recien creado, y no tiene las entradas de League Entry, Match o ChampionStats
            # el last_update sera None
            now = int(time.time())
            if (account_instance.last_update is not None
                and (now - account_instance.last_update) <= 3600):
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
        response = schemas.Response.model_validate(response)
        self._db.commit()
        return response

    def _fetch_account(self) -> schemas.AccountCreate:

        account_response = self.querier.get_account_by_riot_id(
            game_name=self._riot_id.game_name,
            tag_line=self._riot_id.tag_line,
            region=self._server.region
            )
            
        if account_response is not None:
            puuid = account_response.get("puuid")

            summoner_response = self.querier.get_summoner_by_puuid(
                puuid=puuid,
                platform=self._server.platform
            )
            summoner_id = summoner_response.get("id")
            account_id = summoner_response.get("accountId")
            profile_icon_id = summoner_response.get("profileIconId")
            summoner_level = summoner_response.get("summonerLevel")

            return schemas.AccountCreate(
                puuid=puuid,
                summoner_id=summoner_id,
                account_id=account_id,
                game_name=self._riot_id.game_name,
                tag_line=self._riot_id.tag_line,
                profile_icon_id=profile_icon_id,
                summoner_level=summoner_level,
            )
        return None

    def _fetch_league_entries(self) -> list[schemas.LeagueEntryCreate]:
        league_entries = []
        if self._summoner_id is not None:
            league_entries_response = self.querier.get_league_entries_by_summoner_id(
                summoner_id=self._summoner_id,
                platform=self._server.platform
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
                region=self._server.region,
                start_time=settings.SEASON_START,
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


    def _fetch_match_and_participants(
        self,
        match_id
    ) -> tuple[schemas.MatchCreate, list[schemas.ParticipantCreate]] | None:
        match_response = self.querier.get_match_by_match_id(
            match_id=match_id,
            region=self._server.region
        )
        if match_response:
            match_data = match_response.get("info")
            participants_data: list = match_data.get("participants")
            player_data = {}
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
                puuid=self._puuid,
                perk_0=perk0,
                perk_1=perk1,
                riot_id_game_name=player_data.get("riotIdGameName", ""),
                riot_id_tag_line=player_data.get("riotIdTagline", ""),
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

        return None

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
                    match=match,
                    participant=participant,
                )


    def _create_participant(self, participant_data: dict) -> schemas.ParticipantCreate:
        return schemas.ParticipantCreate(
            champion_id=participant_data.get("championId"),
            champion_name=participant_data.get("championName"),
            riot_id_game_name=participant_data.get("riotIdGameName", ""),
            riot_id_tagline=participant_data.get("riotIdTagline", ""),
            team_id=participant_data.get("teamId"),
            team_position=participant_data.get("teamPosition")
        )


    def _create_or_update_champion_stats(self, match: models.Match):

        cs_instance = crud.get_champion_stats(
            self._db,
            account_id=match.account_id,
            name=match.champion_name
        )

        if cs_instance is None:
            wins = 1 if match.win else 0
            cs_instance = crud.create_champion_stats(
                db=self._db,
                account_id=match.account_id,

                champion_stats=schemas.ChampionStatsCreate(
                    name=match.champion_name,
                    kill_avg=round(match.kills, 1),
                    death_avg=round(match.deaths, 1),
                    assist_avg=round(match.assists, 1),
                    kda=self._calculate_kda(match.kills, match.deaths, match.assists),
                    winrate=self._calculate_winrate(wins, 1),
                    games_played=1,
                    wins= 1 if match.win else 0,
                    losses=1 if not match.win else 1,
                )
            )
        else:
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
            new_wins = cs_instance.wins + 1 if match.win else cs_instance.wins
            new_losses = cs_instance.losses + 1 if not match.win else cs_instance.losses
            new_wr = self._calculate_winrate(new_wins, games_played)
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


    def _get_or_create_account_model(self) -> models.Account:
        account_model = crud.get_account_by_game_name_and_tag_line(
            db=self._db,
            game_name=self._riot_id.game_name,
            tag_line=self._riot_id.tag_line
        )
        if account_model is None:
            new_account_data = self._fetch_account()
            self.set_summoner_id(new_account_data.summoner_id)
            self.set_puuid(new_account_data.puuid)
            account_model = crud.create_account(db=self._db, account=new_account_data)

        self.set_summoner_id(account_model.summoner_id)
        self.set_puuid(account_model.puuid)
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
                crud.create_league_entry(
                        db=self._db,
                        league_entry=league_entry,
                        account_id=db_obj.id
                    )

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
                account=db_obj
            )
            
            if match.queue_id == 420 or match.queue_id == 440:
                # Si es una partida de SoloQ o FlexQ
                self._create_or_update_champion_stats(match)

            for participant in participants:
                crud.create_participant(
                    db=self._db,
                    participant=participant,
                    match=match
                )

    @staticmethod
    def _calculate_kda(k: float, d: float, a: float) -> float:
        if d == 0:
            d = 1  # Para evitar division por 0
        return round(((k + a) / d), 2)

    @staticmethod
    def _calculate_winrate(wins: int, games: int) -> int:
        return int((wins / games) * 100)

    @staticmethod
    def _calculate_avg(new_value: int, prev_avg: int, games_played: int) -> float:
        if games_played == 1:
            return round(float(new_value), 2)

        prev_total = prev_avg * (games_played - 1)
        total = prev_total + new_value
        new_avg = total / games_played
        return round(new_avg, 2)
