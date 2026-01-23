from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.infra.db import Database


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async for session in Database.get_session():
        yield session
