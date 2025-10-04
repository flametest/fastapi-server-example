from app.domain.user import User
from app.infra.repository.user_repository import UserRepository
from app.web.api.v1.dependencies.db import DB


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_user_by_username(self, username: str) -> User | None:
        db_user = await self.user_repo.get_user_by_username(username)
        if not db_user:
            return None
        return User.from_db(db_user)

    async def get_user_by_email(self, email: str) -> User | None:
        db_user = await self.user_repo.get_user_by_email(email)
        if not db_user:
            return None
        return User.from_db(db_user)

    async def get_user_by_id(self, user_id: int) -> User | None:
        db_user = await self.user_repo.get_user_by_id(user_id)
        if not db_user:
            return None
        return User.from_db(db_user)


def get_user_service(db: DB) -> UserService:
    user_repo = UserRepository(db)
    return UserService(user_repo=user_repo)
