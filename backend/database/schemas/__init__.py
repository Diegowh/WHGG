'''
Este módulo contiene los DTOs utilizados para transferir
los datos entre la API de Riot Games y la base de datos del backend
'''
from backend.database.schemas.account import (
    Account,
    AccountBase,
    AccountCreate,
    AccountUpdate,
    Response
)
from backend.database.schemas.champion_stats import (
    ChampionStats,
    ChampionStatsBase,
    ChampionStatsCreate,
    ChampionStatsUpdate
)
from backend.database.schemas.league_entry import (
    LeagueEntry,
    LeagueEntryBase,
    LeagueEntryCreate,
    LeagueEntryUpdate
)
from backend.database.schemas.match import (
    Match,
    MatchBase,
    MatchCreate
)
from backend.database.schemas.participant import (
    Participant,
    ParticipantCreate,
    ParticipantBase
)
from backend.database.schemas.request import (
    Request,
    RiotId,
    RiotServer,
)

__all__ = [
    "Account", "AccountBase", "AccountCreate", "AccountUpdate", "Response",
    "ChampionStats", "ChampionStatsBase", "ChampionStatsCreate", "ChampionStatsUpdate",
    "LeagueEntry", "LeagueEntryBase", "LeagueEntryCreate", "LeagueEntryUpdate",
    "Match", "MatchBase", "MatchCreate",
    "Participant", "ParticipantCreate", "ParticipantBase",
    "Request", "RiotId", "RiotServer"
]
