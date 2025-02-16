from typing import Generic, TypeVar, List, Dict, Any, Optional
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.session import DatabaseSession

T = TypeVar('T')


class BaseRepository(Generic[T]):
    """基础仓储接口"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, id: UUID) -> Optional[T]:
        raise NotImplementedError

    async def list_by_ids(self, ids: List[UUID]) -> List[T]:
        raise NotImplementedError

    async def create(self, entity: T) -> T:
        raise NotImplementedError

    async def update(self, entity: T) -> T:
        raise NotImplementedError

    async def delete(self, id: UUID) -> bool:
        raise NotImplementedError

    async def list(self, filters: Dict[str, Any]) -> List[T]:
        raise NotImplementedError

    async def execute_in_transaction(self, func):
        async with DatabaseSession.get_session() as session:
            return await func(session)
