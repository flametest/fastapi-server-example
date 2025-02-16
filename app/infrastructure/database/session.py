from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class DatabaseSession:
    _engine: AsyncEngine = None
    _session_factory: sessionmaker = None

    @classmethod
    def init(cls, connection_string: str):
        cls._engine = create_async_engine(connection_string)
        cls._session_factory = sessionmaker(
            cls._engine, class_=AsyncSession, expire_on_commit=False
        )

    @classmethod
    @asynccontextmanager
    async def get_session(cls) -> AsyncGenerator[AsyncSession, None]:
        if not cls._session_factory:
            raise RuntimeError("Database session not initialized")

        async with cls._session_factory() as session:
            try:
                yield session
                await session.commit()
            except:
                await session.rollback()
                raise
