import pytest
from unittest.mock import patch
from backend.core.riot_querier import RiotQuerier
from backend.database.schemas import RiotServer
from backend.config import Settings


@pytest.fixture
def mock_settings():
    return Settings(RIOT_API_KEY="test_key")


@pytest.fixture
def mock_server():
    return RiotServer(name="EUW")


@pytest.fixture
def riot_querier():
    return RiotQuerier()


def test_get_account_by_riot_id(riot_querier):
    with patch.object(riot_querier, '_fetch', return_value={"puuid": "test_puuid", "gameName": "test_game", "tagLine": "test_tag"}):
        response = riot_querier.get_account_by_riot_id("test_game", "test_tag", "test_region")
        assert response == {"puuid": "test_puuid", "gameName": "test_game", "tagLine": "test_tag"}


def test_get_summoner_by_puuid(riot_querier):
    with patch.object(riot_querier, '_fetch', return_value={"id": "test_id", "accountId": "test_account_id", "puuid": "test_puuid", "profileIconId": 1234, "revisionDate": 1234567890, "summonerLevel": 30}):
        response = riot_querier.get_summoner_by_puuid("test_puuid", "test_platform")
        assert response == {"id": "test_id", "accountId": "test_account_id", "puuid": "test_puuid", "profileIconId": 1234, "revisionDate": 1234567890, "summonerLevel": 30}


def test_get_matches_by_puuid(riot_querier):
    with patch.object(riot_querier, '_fetch', return_value=["match_id_1", "match_id_2"]):
        response = riot_querier.get_matches_by_puuid("test_puuid", "test_region",start_time=1234567890, end_time=1234567891, queue=420, type="ranked", start=0, count=20)
        assert response == ["match_id_1", "match_id_2"]


def test_get_match_by_match_id(riot_querier):
    with patch.object(riot_querier, '_fetch', return_value={"info": "match_details"}):
        response = riot_querier.get_match_by_match_id("match_id_1", "test_platform")
        assert response == {"info": "match_details"}


def test_get_league_entries_by_summoner_id(riot_querier):
    with patch.object(riot_querier, '_fetch', return_value=[{"leagueId": "test_league", "tier": "GOLD", "rank": "I"}]):
        response = riot_querier.get_league_entries_by_summoner_id("test_id", "test_platform")
        assert response == [{"leagueId": "test_league", "tier": "GOLD", "rank": "I"}]

