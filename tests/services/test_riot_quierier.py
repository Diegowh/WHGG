import httpx
import pytest
from unittest.mock import AsyncMock, patch
from backend.services.riot_querier import RiotQuerier
from backend.schemas.riot_server import RiotServer
from backend.config import Settings


@pytest.fixture
def mock_settings():
    return Settings(RIOT_API_KEY="test_key")


@pytest.fixture
def mock_server():
    return RiotServer(name="EUW")


@pytest.fixture
def riot_querier(mock_server, mock_settings):
    return RiotQuerier(server=mock_server, settings=mock_settings)

@pytest.mark.asyncio
async def test_get_account_by_riot_id(riot_querier):
    with patch.object(riot_querier, '_fetch', return_value={"puuid": "test_puuid", "gameName": "test_game", "tagLine": "test_tag"}):
        response = await riot_querier.get_account_by_riot_id("test_game", "test_tag")
        assert response == {"puuid": "test_puuid", "gameName": "test_game", "tagLine": "test_tag"}


@pytest.mark.asyncio
async def test_get_summoner_by_puuid(riot_querier):
    with patch.object(riot_querier, '_fetch', return_value={"id": "test_id", "accountId": "test_account_id", "puuid": "test_puuid", "profileIconId": 1234, "revisionDate": 1234567890, "summonerLevel": 30}):
        response = await riot_querier.get_summoner_by_puuid("test_puuid")
        assert response == {"id": "test_id", "accountId": "test_account_id", "puuid": "test_puuid", "profileIconId": 1234, "revisionDate": 1234567890, "summonerLevel": 30}


@pytest.mark.asyncio
async def test_get_matches_by_puuid(riot_querier):
    with patch.object(riot_querier, '_fetch', return_value=["match_id_1", "match_id_2"]):
        response = await riot_querier.get_matches_by_puuid("test_puuid", start_time=1234567890, end_time=1234567891, queue=420, type="ranked", start=0, count=20)
        assert response == ["match_id_1", "match_id_2"]


@pytest.mark.asyncio
async def test_get_match_by_match_id(riot_querier):
    with patch.object(riot_querier, '_fetch', return_value={"info": "match_details"}):
        response = await riot_querier.get_match_by_match_id("match_id_1")
        assert response == {"info": "match_details"}


@pytest.mark.asyncio
async def test_get_league_entry_by_summoner_id(riot_querier):
    with patch.object(riot_querier, '_fetch', return_value=[{"leagueId": "test_league", "tier": "GOLD", "rank": "I"}]):
        response = await riot_querier.get_league_entry_by_summoner_id("test_id")
        assert response == [{"leagueId": "test_league", "tier": "GOLD", "rank": "I"}]


@pytest.mark.asyncio
async def test_set_server(riot_querier):
    riot_querier._account_endpoint = "/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    riot_querier._matches_endpoint = "/lol/match/v5/matches/by-puuid/{puuid}/ids"
    riot_querier._match_endpoint = "/lol/match/v5/matches/{match_id}"
    riot_querier._summoner_endpoint = "/lol/summoner/v4/summoners/by-puuid/{puuid}"
    riot_querier._league_entry_endpoint = "/lol/league/v4/entries/by-summoner/{summoner_id}"

    assert riot_querier.set_server(riot_querier._account_endpoint) == "europe"
    assert riot_querier.set_server(riot_querier._match_endpoint) == "europe"
    assert riot_querier.set_server(riot_querier._matches_endpoint) == "europe"

    assert riot_querier.set_server(riot_querier._summoner_endpoint) == "euw1"
    assert riot_querier.set_server(riot_querier._league_entry_endpoint) == "euw1"

