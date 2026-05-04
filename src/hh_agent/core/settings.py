from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "HH Agent"
    app_env: str = "local"
    debug: bool = True

    hh_client_id: str = ""
    hh_client_secret: str = ""
    hh_redirect_uri: str = "http://127.0.0.1:8000/auth/hh/callback"

    telegram_bot_token: str = ""

    database_url: str = "sqlite+aiosqlite:///./hh_agent.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
