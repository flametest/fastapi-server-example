import logging
import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import MultiHostUrl
from pydantic import MySQLDsn

ROOT_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve()
print(f"{str(ROOT_DIR)}/.env")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Use top level .envf"{str(ROOT_DIR)}/.env" file
        env_file=f"{str(ROOT_DIR)}/.env",
        env_ignore_empty=True,
        extra="ignore",
    )

    APP_NAME: str

    SERVER_HOST: str = "localhost"
    SERVER_PORT: int = 8080

    API_PREFIX: str = ""

    DATABASE_URL: str

    LOGGING_LEVEL: int = logging.INFO

    # def SQLALCHEMY_DATABASE_URI(self) -> MySQLDsn:
    #     return MultiHostUrl.build(
    #         scheme="",
    #     )


settings: Settings = Settings()
print(settings.dict())
