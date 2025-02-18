from typing import List, Optional

from sqlalchemy import select

from app.domain.interfaces.repository.repository import BaseRepository
from app.infrastructure.persistence.models import Company


class CompanyRepository(BaseRepository[Company]):
    async def get_by_id(self, id: int) -> Optional[Company]:
        query = select(Company).where(Company.id == id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def list_by_ids(self, ids: List[int]) -> List[Company]:
        query = select(Company).where(Company.id.in_(ids))
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, company: Company) -> Company:
        self.session.add(company)
        await self.session.flush()
        return company

    async def get_by_name(self, name: str) -> Optional[Company]:
        query = select(Company).where(Company.name == name)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
