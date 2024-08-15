from pydantic import BaseModel

from src.dtos.account_dto import AccountDTO
from src.dtos.champion_stats_dto import ChampionSatsDto
from src.dtos.league_entry_dto import LeagueEntryDto
from src.dtos.match_dto import MatchDto
from src.dtos.profile_dto import ProfileDto
from src.dtos.summoner_dto import SummonerDTO
from src.models.league_entry import LeagueEntry


class ResponseDto(BaseModel):
    profile: ProfileDto
    league_entries: list[LeagueEntryDto]
    match_history: list[MatchDto]
    champion_stats: list[ChampionSatsDto]