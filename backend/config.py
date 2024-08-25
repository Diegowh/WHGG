from datetime import datetime

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # RiotGames API
    RIOT_API_KEY: str

    # Database
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file='.env')

    # https://dotesports.com/league-of-legends/news/start-and-end-dates-for-all-league-of-legends-seasons
    season_start_timestamp: int = int(datetime(2024, 1, 10).timestamp())

settings = Settings()
