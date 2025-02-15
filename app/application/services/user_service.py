from typing import List
from ..domain.entities.user import User
from ..domain.repositories.user_repository import UserRepository
from ..domain.repositories.company_repository import CompanyRepository
from .commands.user_commands import CreateUserCommand, UpdateUserCommand, ChangeUserCompanyCommand
from .event_handlers.user_event_handlers import UserEventHandler
from ..domain.events.user_events import UserCreatedEvent, UserCompanyChangedEvent
from .event_bus.event_bus import EventBus


class UserApplicationService:
    def __init__(self, user_repository, company_repository):
        self._user_repository = user_repository
        self._company_repository = company_repository
        self._event_bus = EventBus()
        self._init_event_handlers()

    def _init_event_handlers(self):
        # 初始化事件处理器
        handler = UserEventHandler()

        # 注册同步处理器
        self._event_bus.register(UserCreatedEvent, handler.handle_user_created)
        self._event_bus.register(UserCompanyChangedEvent, handler.handle_company_changed)

        # 注册异步处理器
        self._event_bus.register_async(UserCreatedEvent, handler.handle_user_created_async)
        self._event_bus.register_async(UserCompanyChangedEvent, handler.handle_company_changed_async)

    def create_user(self, command: CreateUserCommand) -> User:
        # 验证公司是否存在
        company = self._company_repository.get_by_id(command.company_id)
        if not company:
            raise ValueError("指定的公司不存在")

        # 创建用户实体
        user = User(
            first_name=command.first_name,
            last_name=command.last_name,
            age=command.age,
            gender=command.gender,
            company=company
        )

        # 保存用户
        created_user = self._user_repository.create(user)

        # 同步发布事件
        event = UserCreatedEvent(user_id=created_user.id, company_id=company.id)
        self._event_bus.publish(event)

        return created_user

    async def create_user_async(self, command: CreateUserCommand) -> User:
        user = self.create_user(command)

        # 异步发布事件
        event = UserCreatedEvent(user_id=user.id, company_id=user.company.id)
        await self._event_bus.publish_async(event)

        return user

    def update_user(self, command: UpdateUserCommand) -> User:
        # 获取现有用户
        user = self._user_repository.get_by_id(command.user_id)
        if not user:
            raise ValueError("用户不存在")

        # 更新用户信息
        if command.first_name is not None:
            user.first_name = command.first_name
        if command.last_name is not None:
            user.last_name = command.last_name
        if command.age is not None:
            user.age = command.age
        if command.company_id is not None:
            new_company = self._company_repository.get_by_id(command.company_id)
            if not new_company:
                raise ValueError("指定的公司不存在")
            user.change_company(new_company)

        # 保存更改
        return self._user_repository.save(user)

    def change_user_company(self, command: ChangeUserCompanyCommand) -> User:
        user = self._user_repository.get_by_id(command.user_id)
        if not user:
            raise ValueError("用户不存在")

        new_company = self._company_repository.get_by_id(command.new_company_id)
        if not new_company:
            raise ValueError("指定的新公司不存在")

        old_company = user.company
        user.change_company(new_company)

        updated_user = self._user_repository.save(user)

        # 发布公司变更事件
        event = UserCompanyChangedEvent(
            user_id=user.id,
            old_company=old_company,
            new_company=new_company
        )
        self._event_handler.handle_company_changed(event)

        return updated_user

    def get_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        return self._user_repository.get_all(skip, limit)

    def get_user_by_id(self, user_id: int) -> User:
        user = self._user_repository.get_by_id(user_id)
        if not user:
            raise ValueError("用户不存在")
        return user
