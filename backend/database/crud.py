
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, select
import backend.database.models as models
import backend.database.schemas as schemas
from sqlalchemy.exc import NoResultFound

# ----- CREATE ----- #
def create_account(db: Session, account: schemas.AccountCreate) -> models.Account:
    # En vez de pasar cada keyword a models.Account leyendolo desde schemas.Account
    # Genero un diccionario con account.model_dump()
    # Y se lo paso a los **kwargs de models.Account
    db_account = models.Account(**account.model_dump())
    db.add(db_account)
    db.flush()
    db.refresh(db_account)
    return db_account


def create_champion_stats(db: Session, champion_stats: schemas.ChampionStatsCreate, account_id: int) -> models.ChampionStats:
    db_champion_stats = models.ChampionStats(**champion_stats.model_dump(), account_id=account_id)
    db.add(db_champion_stats)
    db.flush()
    db.refresh(db_champion_stats)
    return db_champion_stats


def create_league_entry(db: Session, league_entry: schemas.LeagueEntryCreate, account_id: int) -> models.LeagueEntry:
    db_league_entry = models.LeagueEntry(**league_entry.model_dump(), account_id=account_id)
    db.add(db_league_entry)
    db.flush()
    db.refresh(db_league_entry)
    return db_league_entry


def create_match(db: Session, account: models.Account, match: schemas.MatchCreate) -> models.Match:
    db_match = models.Match(**match.model_dump(), account_id=account.id)
    db.add(db_match)
    db.flush()
    db.refresh(db_match)
    return db_match


def create_participant(db: Session, match: models.Match, participant: schemas.ParticipantCreate) -> models.Participant:
    db_participant = models.Participant(**participant.model_dump(), match_id=match.id)
    db.add(db_participant)
    db.flush()
    db.refresh(db_participant)
    return db_participant


# ----- READ ----- #
def get_account(db: Session, account_id: int) -> models.Account:
    return db.get(models.Account, account_id)


def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    stmt = select(models.Account).offset(skip).limit(limit)
    return db.execute(stmt).scalars().all()


def get_account_by_puuid(db: Session, puuid: str) -> models.Account:
    stmt = select(models.Account).where(models.Account.puuid == puuid)
    return db.execute(statement=stmt).scalar_one_or_none()


def get_account_by_game_name_and_tag_line(db: Session, game_name: str, tag_line: str) -> models.Account:
    stmt = (
        select(models.Account)
        .where(
            models.Account.game_name == game_name,
            models.Account.tag_line == tag_line
        )
    )
    return db.scalar(stmt)


def get_response(db: Session, db_obj: models.Account):
    stmt = (
        select(models.Account)
        .options(
            joinedload(models.Account.league_entries),
            joinedload(models.Account.matches),
            joinedload(models.Account.champion_stats)
        )
        .where(
            models.Account.id == db_obj.id,
        )
    )
    return db.scalar(stmt)


def get_matches(db: Session, account_id: int, skip: int = 0, limit: int = 100) -> list[models.Match]:
    stmt = (
        select(models.Match)
        .where(models.Match.account_id == account_id)
        .offset(skip)
        .limit(limit)
    )
    return db.execute(stmt).scalars().all()


def get_last_match(db: Session, account_id: int) -> models.Match:
    stmt = (
        select(models.Match)
        .where(models.Match.account_id == account_id)
        .order_by(models.Match.id.desc())
        .limit(1)
    )
    return db.execute(stmt).scalar_one_or_none()
    

def count_matches(db: Session, db_obj: models.Account) -> int:
    return db.scalar(
        select(func.count())
        .select_from(models.Match)
        .where(models.Match.account_id == db_obj.id)
    )


def get_league_entry_by_queue_type(db: Session, account_id: int, queue_type: str) -> models.LeagueEntry:
    stmt = (
        select(models.LeagueEntry)
        .where(
            models.LeagueEntry.account_id == account_id,
            models.LeagueEntry.queue_type == queue_type
        )
    )
    return db.scalar(stmt)
    
    

# ----- UPDATE ----- #
def update_account(db: Session, account: schemas.AccountUpdate) -> models.Account:
    stmt = select(models.Account).where(models.Account.puuid == account.puuid)
    db_account = db.execute(stmt).scalar_one_or_none()
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    for key, value in account.model_dump(exclude_unset=True).items():
        setattr(db_account, key, value)

    db.flush()
    db.refresh(db_account)
    return db_account


def update_account_last_update(db: Session, db_obj: models.Account, last_update: int) -> models.Account:
    db_obj.last_update = last_update
    db.add(db_obj)
    db.flush()
    return db_obj


def update_league_entry(db: Session, db_obj: models.LeagueEntry, obj_in: schemas.LeagueEntryUpdate) -> models.LeagueEntry:
    db_league_entry = db.get(models.LeagueEntry, db_obj.id)
    if not db_league_entry:
        raise HTTPException(status_code=404, detail="LeagueEntry not found")

    for key, value in obj_in.model_dump(exclude_unset=True).items():
        setattr(db_league_entry, key, value)
        
    db.flush()
    db.refresh(db_league_entry)
    return db_league_entry


def update_champion_stats(db: Session, id: int, champion_stats: schemas.ChampionStatsUpdate) -> models.ChampionStats:
    stmt = select(models.ChampionStats).where(models.ChampionStats.id == id)
    db_champion_stats = db.execute(stmt).scalar_one_or_none()
    if not db_champion_stats:
        raise HTTPException(status_code=404, detail="ChampionStats not found")
    
    for key, value in champion_stats.model_dump(exclude_unset=True).items():
        setattr(db_champion_stats, key, value)
        
    db.flush()
    db.refresh(db_champion_stats)
    return db_champion_stats

    
def get_or_create_champion_stats(db: Session, account_id: int, champion_stats: schemas.ChampionStatsUpdate) -> models.ChampionStats:
    stmt = (
        select(models.ChampionStats)
        .where(
            models.ChampionStats.account_id == account_id,
            models.ChampionStats.name == champion_stats.name
        )
    )
    
    try:
        champion_stats_entry = db.execute(stmt).scalar_one()
        
        for key, value in champion_stats.model_dump(exclude_unset=True).items():
            setattr(champion_stats_entry, key, value)
        
        db.flush()
        db.refresh(champion_stats_entry)
        return champion_stats_entry

    except NoResultFound:
        new_champion_stats = models.ChampionStats(
            account_id=account_id,
            **champion_stats.model_dump()
        )
        db.add(new_champion_stats)
        db.flush()
        db.refresh(new_champion_stats)
        return new_champion_stats

def get_champion_stats(db: Session, account_id: int, name: str) -> models.ChampionStats | None:
    stmt = (
        select(models.ChampionStats)
        .where(
            models.ChampionStats.account_id == account_id,
            models.ChampionStats.name == name
        )
    )
    return db.execute(stmt).scalars().one_or_none()
    

def _get_or_create(db: Session, model, **kwargs):
    stmt = select(model).filter_by(**kwargs)
    instance = db.execute(stmt).scalar_one_or_none()
    if instance:
        return instance, False
    
    else:
        instance = model(**kwargs)
        db.add(instance)
        db.flush()
        return instance, True