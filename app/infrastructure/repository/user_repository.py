from uuid import UUID
from typing import List, Optional
from sqlalchemy import select
from app.domain.interfaces.repository.repository import BaseRepository
from app.infrastructure.persistence.models import User


class UserRepository(BaseRepository[User]):
    async def get_by_id(self, id: UUID) -> Optional[User]:
        query = select(User).where(User.id == id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def list_by_ids(self, ids: List[UUID]) -> List[User]:
        query = select(User).where(User.id.in_(ids))
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, User: User) -> User:
        self.session.add(User)
        await self.session.flush()
        return User

    async def get_by_email(self, email: str) -> Optional[User]:
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
