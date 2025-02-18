from app.application.commands.models.user_command import CreateUserCommand, UpdateUserCommand, \
    ChangeUserCompanyCommand
from app.application.services.user_service import UserApplicationService


class UserCommands:
    def __init__(self, user_service: UserApplicationService):
        self.user_service = user_service

    async def create_user(self, command: CreateUserCommand) -> int:
        """创建用户"""
        user = await self.user_service.create_user(command)
        return user.id

    async def update_user(self, command: UpdateUserCommand) -> bool:
        """更新用户信息"""
        user = await self.user_service.update_user(command)
        return True

    async def change_user_company(self, command: ChangeUserCompanyCommand) -> bool:
        """更改用户所属公司"""
        user = await self.user_service.change_user_company(command)
        return True

    async def delete_user(self, user_id: int) -> bool:
        """删除用户"""
        return await self.user_service.delete_user(user_id)
