from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    APP_NAME: str = "FastAPI Server"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    DATABASE_URL: str
    REDIS_URL: str
    JWT_SECRET: str