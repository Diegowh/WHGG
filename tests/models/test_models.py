import pytest

from src.models import *


def test_account_creation(session):
    account = Account(
        puuid="unique-puuid",
        summonerId="unique-summonerId",
        accountId="unique-accountId",
        gameName="TestGame",
        tagLine="TestTag",
        profileIconId=123,
        revisionDate=123456789,
        summonerLevel=30
    )

    session.add(account)
    session.commit()
    
    retrieved_account = session.query(Account).filter_by(puuid="unique-puuid").one()
    assert retrieved_account.puuid == "unique-puuid"
    assert retrieved_account.summonerId == "unique-summonerId"
    assert retrieved_account.accountId == "unique-accountId"
    assert retrieved_account.gameName == "TestGame"
    assert retrieved_account.tagLine == "TestTag"
    assert retrieved_account.profileIconId == 123
    assert retrieved_account.revisionDate == 123456789
    assert retrieved_account.summonerLevel == 30
    
def test_account_league_entries(session):
    account = Account(
        puuid="unique-puuid",
        summonerId="unique-summonerId",
        accountId="unique-accountId",
        gameName="TestGame",
        tagLine="TestTag",
        profileIconId=123,
        revisionDate=123456789,
        summonerLevel=30
    )
    
    league_entry = LeagueEntry(
        leagueId="leagueId",
        queueType="RANKED_SOLO_5x5",
        tier="GOLD",
        rank="I",
        summonerId="unique-summonerId",
        leaguePoints=100,
        wins=10,
        losses=5,
        hotStreak=True,
        veteran=False,
        freshBlood=False,
        inactive=False
    )
    
    account.league_entries.append(league_entry)
    session.add(account)
    session.commit()
    
    retrieved_account = session.query(Account).filter_by(puuid="unique-puuid").one()
    assert len(retrieved_account.league_entries) == 1
    
    retrieved_league_entry = retrieved_account.league_entries[0]
    assert retrieved_league_entry.leagueId == "leagueId"
    assert retrieved_league_entry.queueType == "RANKED_SOLO_5x5"
    assert retrieved_league_entry.tier == "GOLD"
    assert retrieved_league_entry.rank == "I"
    assert retrieved_league_entry.summonerId == "unique-summonerId"
    assert retrieved_league_entry.leaguePoints == 100
    assert retrieved_league_entry.wins == 10
    assert retrieved_league_entry.losses == 5
    assert retrieved_league_entry.hotStreak is True
    assert retrieved_league_entry.veteran is False
    assert retrieved_league_entry.freshBlood is False
    assert retrieved_league_entry.inactive is False