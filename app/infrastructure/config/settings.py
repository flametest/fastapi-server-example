from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # 应用基础配置
    APP_NAME: str = "fastapi-server-example"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # 服务器配置
    SERVER_HOST: str = "localhost"
    SERVER_PORT: int = 8080
    API_PREFIX: str = "/api/v1"

    # 数据库配置
    DATABASE_URL: str = "mysql+pymysql://root:root@localhost:3306/test"
    REDIS_URL: str = "redis://localhost:6379/0"

    # 认证配置
    JWT_SECRET: str = "your-secret-key"

    # 日志配置
    LOG_LEVEL: int = 20  # INFO
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
