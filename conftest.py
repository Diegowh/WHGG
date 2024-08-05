# conftest.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from src.models.base import Base
from src.models.account.account import Account
from src.models.league.league_entry import LeagueEntry

@pytest.fixture(scope='module')
def engine():
    return create_engine('sqlite:///:memory:')

@pytest.fixture(scope='module')
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)
    clear_mappers()

@pytest.fixture(scope='function')
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    
    yield session

    session.close()
    transaction.rollback()
    connection.close()
