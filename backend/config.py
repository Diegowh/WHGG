'''
Modulo que centraliza y controla la configuración del backend.

Define una clase Settings que encapsula los detalles de configuración,
como las API keys, URL  de la base de datos, etc.
'''
from datetime import datetime

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Centraliza y controla los ajustes de la aplicación.
    
    Esta clase utiliza `BaseSettings` de Pydantic para cargar automáticamente los
    valores de configuración desde variables de entorno o un archivo `.env`. Incluye
    configuraciones para la clave API de RiotGames, la URL de la base de datos y otras
    constantes específicas de la aplicación.

    Attrs:
        RIOT_API_KEY (str): La clave para interactuar con la API de Riot Games.
        DATABASE_URL (str): La URL de la conexión a la base de datos.
        SEASON_START (int): El timestamp Unix que marca el inicio de la
            temporada actual de League of Legends.
    """

    RIOT_API_KEY: str
    DATABASE_URL: str
    # https://dotesports.com/league-of-legends/news/start-and-end-dates-for-all-league-of-legends-seasons
    SEASON_START: int = int(datetime(2024, 1, 10).timestamp())

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
