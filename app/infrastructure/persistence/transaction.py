from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.persistence.databases.session import DatabaseSession



# 使用 TransactionManager
# await TransactionManager.execute_in_transaction(some_func)

class TransactionManager:
    @staticmethod
    async def execute_in_transaction(func):
        async with DatabaseSession.get_session() as session:
            return await func(session)