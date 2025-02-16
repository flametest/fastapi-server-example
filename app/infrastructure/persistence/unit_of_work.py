from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database.session import DatabaseSession


# 或者使用 UnitOfWork
# async with UnitOfWork() as uow:
# 在事务中执行操作
# await repository.create(entity)

class UnitOfWork:
    def __init__(self):
        self._session: AsyncSession | None = None

    async def __aenter__(self):
        self._session = await DatabaseSession.get_session().__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.__aexit__(exc_type, exc_val, exc_tb)
        self._session = None

    @property
    def session(self) -> AsyncSession:
        return self._session
