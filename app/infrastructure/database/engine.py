from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from typing import Optional

class DatabaseEngine:
    _instance: Optional[AsyncEngine] = None
    
    @classmethod
    def init(cls, connection_string: str) -> None:
        if not cls._instance:
            cls._instance = create_async_engine(
                connection_string,
                echo=False,
                pool_size=5,
                max_overflow=10
            )
    
    @classmethod
    def get_engine(cls) -> AsyncEngine:
        if not cls._instance:
            raise RuntimeError("Database engine not initialized")
        return cls._instance