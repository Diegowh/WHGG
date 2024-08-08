# conftest.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from src.models.base import Base


# scope='module' para crear el motor de la base de datos
# una vez por modulo de prueba
@pytest.fixture(scope='module')
def engine():
    """Fixture para la base de datos en memoria."""
    return create_engine('sqlite:///:memory:')

# scope='module' asegura que las tablas se crean y eliminan
# una sola vez por modulo
@pytest.fixture(scope='module')
def tables(engine):
    """Fixture para crear y eliminar tablas en la base de datos."""
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)
    # Limpia cualquier mapeo registrado en SQLAlchemy
    # para evitar conflictos si se ejecutan multiples
    # pruebas que involucren mapeos
    clear_mappers() 

# scope='function' asegura que cada prueba obtenga
# una nueva sesion de base de datos para asegurar que
# las pruebas no interfieran entre si
@pytest.fixture(scope='function')
def session(engine, tables):
    """Fixture para la sesión de base de datos, que se usa en cada función de prueba."""
    connection = engine.connect()
    # Para garantizar que cada prueba empiece con una base
    # de datos limpia y revertir cualquier cambio hecho
    # durante la prueba
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    
    yield session

    session.close()
    transaction.rollback()
    connection.close()
