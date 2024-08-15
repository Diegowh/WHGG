from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "WHGG"

    # RiotGames API
    RIOT_API_KEY: str

    # Database
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    model_config = SettingsConfigDict(env_file='.env')
