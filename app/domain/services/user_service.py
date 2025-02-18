from typing import Dict, Any, List

from app.domain.aggregates.user import UserAggregate
from app.domain.exceptions.user_exceptions import UserNotFoundError, CompanyNotFoundError
from app.infrastructure.persistence.repository.company_repository import CompanyRepository
from app.infrastructure.persistence.repository.user_repository import UserRepository


class UserService:
    def __init__(
            self,
            user_repository: UserRepository,
            company_repository: CompanyRepository
    ):
        self._user_repository = user_repository
        self._company_repository = company_repository

    async def create_user(self, user_data: Dict[str, Any]) -> UserAggregate:
        # 验证公司是否存在
        company = await self._company_repository.get_by_id(user_data["company_id"])
        if not company:
            raise CompanyNotFoundError(f"公司不存在: {user_data['company_id']}")

        # 创建用户聚合根
        user = UserAggregate(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            age=user_data["age"],
            gender=user_data["gender"],
            company_id=company.id
        )

        # 保存用户
        return await self._user_repository.create(user)

    async def update_user(self, user_id: int, update_data: Dict[str, Any]) -> UserAggregate:
        # 获取现有用户
        user = await self._user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"用户不存在: {user_id}")

        # 如果要更新公司，先验证新公司是否存在
        if "company_id" in update_data:
            company = await self._company_repository.get_by_id(update_data["company_id"])
            if not company:
                raise CompanyNotFoundError(f"公司不存在: {update_data['company_id']}")

        # 更新用户信息
        user.update(update_data)

        # 保存更改
        return await self._user_repository.create(user)

    async def change_user_company(self, user_id: int, new_company_id: int) -> UserAggregate:
        # 获取用户
        user = await self.get_user_by_id(user_id)
        if not user:
            raise UserNotFoundError(user_id)

        # 验证新公司是否存在
        new_company = await self._company_repository.get_by_id(new_company_id)
        if not new_company:
            raise CompanyNotFoundError(new_company_id)

        # 更改用户所属公司
        user.assign_company(new_company)

        # 保存更改
        return await self._user_repository.create(user)

    async def delete_user(self, user_id: int) -> bool:
        # 验证用户是否存在
        user = await self._user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(user_id)

        # 删除用户
        return await self._user_repository.delete(user_id)

    async def get_users(self, skip: int = 0, limit: int = 100) -> List[UserAggregate]:
        return await self._user_repository.get_all(skip=skip, limit=limit)

    async def get_user_by_id(self, user_id: int) -> UserAggregate:
        user = await self._user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundError(user_id)
        company = None
        if user.company_id:
            company = await self._company_repository.get_by_id(user.company_id)
        return UserAggregate(id=user.id, username=user.username, email=user.email,
                             gender=user.gender, company=company)
