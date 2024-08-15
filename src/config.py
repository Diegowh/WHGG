from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "WHGG"
    RIOT_API_KEY: str

    model_config = SettingsConfigDict(env_file='.env')
