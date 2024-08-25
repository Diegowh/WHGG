from unittest.mock import MagicMock
from httpx import patch
import pytest
from backend.core.data_manager import DataManager


class TestDataManager:
    
    @pytest.mark.parametrize("k, d, a, expected", [
        (10, 5, 5, 3.0),          # Caso general
        (10, 0, 5, 15.0),         # d=0, se debe ajustar a 1
        (0, 1, 0, 0.0),           # Todos los valores cero
        (5, 2, 10, 7.5),          # Otros valores para verificar
    ])
    def test_calculate_kda(self, k, d, a, expected):
        result = DataManager._calculate_kda(k, d, a)
        assert result == expected
        
        
    @pytest.mark.parametrize("wins, games, expected", [
        (10, 20, 50),             # Caso general
        (0, 10, 0),               # Sin victorias
        (10, 0, 0),               # Sin juegos, debería ser manejado para evitar división por cero
        (25, 50, 50),             # Otros valores para verificar
    ])
    def test_calculate_winrate(self, wins, games, expected):
        if games == 0:
            with pytest.raises(ZeroDivisionError):
                DataManager._calculate_winrate(wins, games)
        else:
            result = DataManager._calculate_winrate(wins, games)
            assert result == expected
            
    @pytest.mark.parametrize("new_value, prev_avg, games_played, expected", [
        (10, 5, 2, 7.5),          # Caso general
        (0, 0, 1, 0.0),           # Todos los valores cero
        (10, 0, 1, 10.0),         # Prueba con promedio previo cero
        (30, 10, 3, 16.67),        # Otros valores para verificar
    ])
    def test_calculate_avg(self, new_value, prev_avg, games_played, expected):
        result = DataManager._calculate_avg(new_value, prev_avg, games_played)
        assert result == expected
        
        
    @pytest.fixture
    def data_manager(self):
        return DataManager()
    

    @pytest.fixture
    def mock_db_session(self):
        return MagicMock()
    
    @pytest.fixture
    def mock_riot_querier(self):
        with patch("backend.core.riot_querier.RiotQuerier") as mock:
            yield mock
    
    def test_setters(self, data_manager):
        data_manager.set_game_name('GameName')
        data_manager.set_tag_line('TagLine')
        data_manager.set_region('Region')
        data_manager.set_platform('Platform')
        data_manager.set_summoner_id('SummonerId')
        data_manager.set_puuid('Puuid')
        
        assert data_manager._game_name == 'GameName'
        assert data_manager._tag_line == 'TagLine'
        assert data_manager._region == 'Region'
        assert data_manager._platform == 'Platform'
        assert data_manager._summoner_id == 'SummonerId'
        assert data_manager._puuid == 'Puuid'
