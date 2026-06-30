from functools import lru_cache

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # -----------------------------
    # Application
    # -----------------------------
    APP_NAME: str = "Gmail AI Assistant"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # -----------------------------
    # PostgreSQL
    # -----------------------------
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    # -----------------------------
    # OpenAI
    # -----------------------------
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-5"

    # -----------------------------
    # Gmail
    # -----------------------------
    GMAIL_MAX_RESULTS: int = 10

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=True,
    )

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return (
            "postgresql+psycopg://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()