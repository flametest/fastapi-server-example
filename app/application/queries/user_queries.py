from typing import Optional, List
from app.infrastructure.repository.user_repository import UserRepository
from app.interfaces.schemas.user import UserDetail


class UserQueries:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_user_by_id(self, user_id: int) -> Optional[UserDetail]:
        user = await self.user_repository.get_by_id(user_id)
        if user:
            return UserDetail.model_validate(user)
        return None

    async def get_user_by_email(self, email: str) -> Optional[UserDetail]:
        user = await self.user_repository.get_by_email(email)
        if user:
            return UserDetail.model_validate(user)
        return None

    async def get_users(self, skip: int = 0, limit: int = 10) -> List[UserDetail]:
        users = await self.user_repository.get_all(skip=skip, limit=limit)
        return [UserDetail.model_validate(user) for user in users]

    async def search_users(self, keyword: str) -> List[UserDetail]:
        users = await self.user_repository.search(keyword)
        return [UserDetail.model_validate(user) for user in users]
