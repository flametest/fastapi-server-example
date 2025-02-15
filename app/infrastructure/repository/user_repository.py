from typing import List, Optional
from sqlalchemy import select, and_
from app.domain.interfaces.repository.repository import BaseRepository
from app.infrastructure.persistence.models import User


class UserRepository(BaseRepository[User]):
    async def get_by_id(self, id: int) -> Optional[User]:
        query = select(User).where(and_(User.id == id))
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def list_by_ids(self, ids: List[int]) -> List[User]:
        query = select(User).where(User.id.in_(ids))
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def create(self, user: User) -> User:
        self.session.add(user)
        await self.session.flush()
        return user

    async def get_by_email(self, email: str) -> Optional[User]:
        query = select(User).where(and_(User.email == email))
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
