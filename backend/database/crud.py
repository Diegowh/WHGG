
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

import backend.database.models as models
import backend.database.schemas as schemas


# ----- CREATE ----- #
def create_account(db: Session, account: schemas.AccountCreate) -> models.Account:
    # En vez de pasar cada keyword a models.Account leyendolo desde schemas.Account
    # Genero un diccionario con account.model_dump()
    # Y se lo paso a los **kwargs de models.Account
    db_account = models.Account(**account.model_dump())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def create_champion_stats(db: Session, champion_stats: schemas.ChampionStatsCreate, account_id: int) -> models.ChampionStats:
    db_champion_stats = models.ChampionStats(**champion_stats.model_dump(), account_id=account_id)
    db.add(db_champion_stats)
    db.commit()
    db.refresh(db_champion_stats)
    return db_champion_stats


def create_league_entry(db: Session, league_entry: schemas.LeagueEntryCreate, account_id: int) -> models.LeagueEntry:
    db_league_entry = models.LeagueEntry(**league_entry.model_dump(), account_id=account_id)
    db.add(db_league_entry)
    db.commit()
    db.refresh(db_league_entry)
    return db_league_entry


def create_match(db: Session, match: schemas.MatchCreate, account_id: int) -> models.Match:
    db_match = models.Match(**match.model_dump(), account_id=account_id)
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match


def create_participant(db: Session, participant: schemas.ParticipantCreate, match_id: int) -> models.Participant:
    db_participant = models.Participant(**participant.model_dump(), match_id=match_id)
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant


# ----- READ ----- #
def get_account(db: Session, account_id: int) -> models.Account | None:
    return db.query(models.Account).filter(models.Account.id == account_id).first()


def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Account).offset(skip).limit(limit).all()


def get_account_by_puuid(db: Session, puuid: str) -> models.Account | None:
    return db.query(models.Account).filter(models.Account.puuid == puuid).first()


def get_account_by_game_name_and_tag_line(db: Session, game_name: str, tag_line: str) -> models.Account:
    return (
        db.query(models.Account)
        .options(
            joinedload(models.Account.league_entries),
            joinedload(models.Account.matches),
            joinedload(models.Account.champion_stats)
        )
        .filter(models.Account.game_name == game_name, models.Account.tag_line == tag_line)
        .first()
    )


def get_matches(db: Session, account_id: int, skip: int = 0, limit: int = 100) -> list[models.Match]:
    return (
        db.query(models.Match)
        .filter(models.Match.account_id == account_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


# ----- UPDATE ----- #
def update_account(db: Session, account: schemas.AccountUpdate) -> models.Account:
    db_account = db.query(models.Account).filter(models.Account.puuid == account.puuid).first()
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    for field, value in account.model_dump(exclude_unset=True).items():
        setattr(db_account, field, value)

    db.commit()
    db.refresh(db_account)
    return db_account
