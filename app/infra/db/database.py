from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config.settings import settings


class Database:
    _engine: AsyncEngine | None = None
    _sessionmaker: async_sessionmaker[AsyncSession] | None = None

    @classmethod
    def init(cls) -> AsyncEngine:
        if cls._engine is None:
            cls._engine = create_async_engine(
                settings.DATABASE_URL,
                echo=settings.ENV == "local",
                pool_pre_ping=True,
                pool_size=10,
                max_overflow=20,
            )
            cls._sessionmaker = async_sessionmaker(
                cls._engine,
                class_=AsyncSession,
                expire_on_commit=False,
            )
        return cls._engine

    @classmethod
    async def close(cls) -> None:
        if cls._engine:
            await cls._engine.dispose()
            cls._engine = None
            cls._sessionmaker = None

    @classmethod
    async def get_session(cls) -> AsyncGenerator[AsyncSession, None]:
        if cls._sessionmaker is None:
            cls.init()
        async with cls._sessionmaker() as session:  # type: ignore
            try:
                yield session
            except Exception:
                await session.rollback()
                raise
