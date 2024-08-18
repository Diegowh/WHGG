from sqlalchemy.exc import IntegrityError
import pytest

from backend.database.models import *


def test_account_creation(session):
    account = Account(
        puuid="unique-puuid",
        summoner_id="unique-summonerId",
        account_id="unique-accountId",
        game_name="TestGame",
        tag_line="TestTag",
        profile_iconId=123,
        summoner_level=30,
        last_update=123456789
    )

    session.add(account)
    session.commit()
    
    retrieved_account = session.query(Account).filter_by(puuid="unique-puuid").one()
    
    assert retrieved_account.puuid == "unique-puuid"
    assert retrieved_account.summoner_id == "unique-summonerId"
    assert retrieved_account.account_id == "unique-accountId"
    assert retrieved_account.game_name == "TestGame"
    assert retrieved_account.tag_line == "TestTag"
    assert retrieved_account.profile_iconId == 123
    assert retrieved_account.summoner_level == 30
    assert retrieved_account.last_update == 123456789

def test_champion_stats_creation(session):
    account = Account(
        puuid="unique-puuid",
        summoner_id="unique-summonerId",
        account_id="unique-accountId",
        game_name="TestGame",
        tag_line="TestTag",
        profile_iconId=123,
        summoner_level=30,
        last_update=123456789
    )

    champion_stats = ChampionStats(
        account_id=account.id,
        name="TestChampion",
        kda=3.5,
        kill_avg=5.0,
        death_avg=2.0,
        assist_avg=4.0,
        winrate=60,
        games_played=100
    )

    account.champion_stats.append(champion_stats)

    session.add(account)
    session.commit()

    retrieved_account = session.query(Account).filter_by(puuid='unique-puuid').one()

    assert len(retrieved_account.champion_stats) == 1
    
    retrieved_champion_stats = retrieved_account.champion_stats[0]
    assert retrieved_champion_stats.name == "TestChampion"
    assert retrieved_champion_stats.kda == 3.5
    assert retrieved_champion_stats.kill_avg == 5.0
    assert retrieved_champion_stats.death_avg == 2.0
    assert retrieved_champion_stats.assist_avg == 4.0
    assert retrieved_champion_stats.winrate == 60
    assert retrieved_champion_stats.games_played == 100
    assert retrieved_champion_stats.account_id == retrieved_account.id


def test_league_entry_creation(session):
    account = Account(
        puuid="unique-puuid",
        summoner_id="unique-summonerId",
        account_id="unique-accountId",
        game_name="TestGame",
        tag_line="TestTag",
        profile_iconId=123,
        summoner_level=30,
        last_update=123456789
    )
    
    league_entry = LeagueEntry(
        account_id=account.id,
        queue_type="RANKED_SOLO_5x5",
        tier="DIAMOND",
        rank="IV",
        league_points=100,
        wins=10,
        losses=5,
    )
    
    account.league_entries.append(league_entry)

    session.add(account)
    session.commit()
    
    retrieved_account = session.query(Account).filter_by(puuid="unique-puuid").one()
    assert len(retrieved_account.league_entries) == 1
    
    retrieved_league_entry = retrieved_account.league_entries[0]
    assert retrieved_league_entry.queue_type == "RANKED_SOLO_5x5"
    assert retrieved_league_entry.tier == "DIAMOND"
    assert retrieved_league_entry.rank == "IV"
    assert retrieved_league_entry.league_points == 100
    assert retrieved_league_entry.wins == 10
    assert retrieved_league_entry.losses == 5


def test_match_creation(session):
    account = Account(
        puuid="unique-puuid",
        summoner_id="unique-summonerId",
        account_id="unique-accountId",
        game_name="TestGame",
        tag_line="TestTag",
        profile_iconId=123,
        summoner_level=30,
        last_update=123456789
    )

    match = Match(
        account_id=account.id,
        match_id="match-id",
        game_creation=1234567890,
        game_duration=3600,
        game_end_timestamp=1234567891,
        game_mode="Classic",
        game_start_timestamp=1234567890,
        game_type="Ranked",
        game_version="13.12",
        queue_id=420
    )

    account.matches.append(match)

    session.add(account)
    session.commit()

    retrieved_account = session.query(Account).filter_by(puuid="unique-puuid").one()

    assert len(retrieved_account.matches) == 1
    retrieved_match = retrieved_account.matches[0]
    assert retrieved_match.match_id == "match-id"
    assert retrieved_match.game_creation == 1234567890
    assert retrieved_match.game_duration == 3600
    assert retrieved_match.game_end_timestamp == 1234567891
    assert retrieved_match.game_mode == "Classic"
    assert retrieved_match.game_start_timestamp == 1234567890
    assert retrieved_match.game_type == "Ranked"
    assert retrieved_match.game_version == "13.12"
    assert retrieved_match.queue_id == 420

    assert retrieved_match.account_id == retrieved_account.id
    assert retrieved_match.account == retrieved_account


def test_participant_creation(session):
    account = Account(
        puuid="unique-puuid",
        summoner_id="unique-summonerId",
        account_id="unique-accountId",
        game_name="TestGame",
        tag_line="TestTag",
        profile_iconId=123,
        summoner_level=30,
        last_update=123456789
    )
    session.add(account)
    session.commit()

    match = Match(
        account_id=account.id,
        match_id="match-id",
        game_creation=1234567890,
        game_duration=3600,
        game_end_timestamp=1234567891,
        game_mode="Classic",
        game_start_timestamp=1234567890,
        game_type="Ranked",
        game_version="13.12",
        queue_id=420
    )
    session.add(match)
    session.commit()
    
    participant = Participant(
        match_id=match.id,
        assists=5,
        champ_level=10,
        champion_id=123,
        champion_name="TestChampion",
        deaths=2,
        gold_earned=1500,
        individual_position="Top",
        item_0=1001,
        item_1=1002,
        item_2=1003,
        item_3=1004,
        item_4=1005,
        item_5=1006,
        item_6=0,
        kills=8,
        lane="Top",
        participant_id=1,
        perk_0=8000,
        perk_1=8100,
        puuid="unique-puuid-participant",
        riot_id_game_name="TestGameName",
        riot_id_tagline="TestTagline",
        summoner_1_id=1,
        summoner_2_id=2,
        summoner_id="unique-summonerId-participant",
        team_id=100,
        team_position="Top",
        total_damage_dealt_to_champions=20000,
        total_minions_killed=150,
        vision_score=10,
        wards_placed=5,
        win=True
    )

    match.participants.append(participant)

    session.commit()

    retrieved_match = session.query(Match).filter_by(match_id="match-id").one()

    assert len(retrieved_match.participants) == 1
    retrieved_participant = retrieved_match.participants[0]
    assert retrieved_participant.champion_name == "TestChampion"
    assert retrieved_participant.kills == 8
    assert retrieved_participant.deaths == 2
    assert retrieved_participant.assists == 5
    assert retrieved_participant.gold_earned == 1500

    assert retrieved_participant.match_id == retrieved_match.id
    assert retrieved_participant.match == retrieved_match

    assert retrieved_match.account_id == account.id
    assert retrieved_match.account == account


def test_account_puuid_not_null(session):
    account = Account(
        summoner_id="unique-summonerId",
        account_id="unique-accountId",
        game_name="TestGame",
        tag_line="TestTag",
        profile_iconId=123,
        summoner_level=30,
        last_update=123456789
    )

    session.add(account)
    
    with pytest.raises(IntegrityError):
        session.commit()