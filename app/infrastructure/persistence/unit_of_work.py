from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.session import DatabaseSession


# 1. 在进入上下文时自动开始事务
# 2. 在退出时自动提交或回滚事务
# 3. 异常时自动回滚
# 4. 保证会话正确关闭

# 或者使用 UnitOfWork
# async with UnitOfWork() as uow:
# 在事务中执行操作
# await repository.create(entity)

class UnitOfWork:

    def __init__(self, session: AsyncSession):
        self._session = session

    async def __aenter__(self):
        self._session = await DatabaseSession.get_session().__aenter__()
        # 开始事务
        await self._session.begin()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                # 如果没有异常发生，提交事务
                await self._session.commit()
            else:
                # 如果有异常，回滚事务
                await self._session.rollback()
        finally:
            # 确保会话被正确关闭
            await self._session.__aexit__(exc_type, exc_val, exc_tb)
            self._session = None

    @property
    def session(self) -> AsyncSession:
        return self._session
