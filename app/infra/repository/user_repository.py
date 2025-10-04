from sqlalchemy import select

from app.infra.models import UserModel
from app.web.api.v1.dependencies.db import DB


class UserRepository:
    def __init__(self, db: DB):
        self.db = db

    async def get_user_by_username(
        self,
        username: str,
    ) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.username == username)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_user_by_email(
        self,
        email: str,
    ) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.email == email)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_user_by_id(self, user_id: int) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()
