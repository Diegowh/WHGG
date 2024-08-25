'''
Este módulo contiene los modelos SQLAlchemy que representan las tablas de 
la base de datos.
'''
from backend.database.models.account import Account
from backend.database.models.champion_stats import ChampionStats
from backend.database.models.league_entry import LeagueEntry
from backend.database.models.match import Match
from backend.database.models.participant import Participant
from backend.database.models.version import Version


__all__ = [
    "Account", "ChampionStats", "LeagueEntry", "Match", "Participant", "Version"
]
