import logging

from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.enum import Environment


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    APP_NAME: str = "fastapi-server-example"
    ENV: Environment = Environment.DEV

    SERVER_HOST: str = "localhost"
    SERVER_PORT: int = 8080

    API_PREFIX: str = ""

    DATABASE_URL: str = "sqlite:///:memory:"

    LOGGING_LEVEL: int = logging.INFO

    """
    def SQLALCHEMY_DATABASE_URI(self) -> MySQLDsn:
    return MultiHostUrl.build(
        scheme="",
    )
    """


settings: Settings = Settings()
