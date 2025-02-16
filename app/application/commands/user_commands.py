from pydantic import BaseModel
from app.domain.services.user_service import UserService


class CreateUserCommand(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str
    company_id: int


class UpdateUserCommand(BaseModel):
    user_id: int
    first_name: str | None = None
    last_name: str | None = None
    age: int | None = None
    company_id: int | None = None


class ChangeUserCompanyCommand(BaseModel):
    user_id: int
    new_company_id: int


class UserCommands:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def create_user(self, command: CreateUserCommand) -> int:
        """创建用户"""
        user = await self.user_service.create_user({
            "first_name": command.first_name,
            "last_name": command.last_name,
            "age": command.age,
            "gender": command.gender,
            "company_id": command.company_id
        })
        return user.id

    async def update_user(self, command: UpdateUserCommand) -> bool:
        """更新用户信息"""
        update_data = {k: v for k, v in command.dict().items() if v is not None}
        del update_data["user_id"]
        return await self.user_service.update_user(command.user_id, update_data)

    async def change_user_company(self, command: ChangeUserCompanyCommand) -> bool:
        """更改用户所属公司"""
        return await self.user_service.change_user_company(
            command.user_id,
            command.new_company_id
        )

    async def delete_user(self, user_id: int) -> bool:
        """删除用户"""
        return await self.user_service.delete_user(user_id)
