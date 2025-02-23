from app.application.commands.models.user_command import CreateUserCommand, UpdateUserCommand, \
    ChangeUserCompanyCommand
from app.application.event_bus.event_bus import EventBus
from app.application.event_handlers.user_event_handlers import UserEventHandler
from app.domain.aggregates.user import UserAggregate
from app.domain.events.user_events import UserCreatedEvent, UserCompanyChangedEvent
from app.domain.services.user_service import UserService as DomainUserService
from app.infrastructure.persistence.unit_of_work import UnitOfWork


class UserApplicationService:
    def __init__(
            self,
            domain_service: DomainUserService,
            event_bus: EventBus,
            unit_of_work: UnitOfWork
    ):
        self._domain_service = domain_service
        self._event_bus = event_bus
        self._uow = unit_of_work
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

    async def create_user(self, command: CreateUserCommand) -> UserAggregate:
        async with self._uow:  # 使用工作单元管理事务
            # 通过领域服务创建用户
            user = await self._domain_service.create_user({
                "first_name": command.first_name,
                "last_name": command.last_name,
                "age": command.age,
                "gender": command.gender,
                "company_id": command.company_id
            })

            # 发布事件
            event = UserCreatedEvent(user_id=user.id, company_id=user.company.id)
            await self._event_bus.publish(event)

        return user

    async def update_user(self, command: UpdateUserCommand) -> UserAggregate:
        # 通过领域服务更新用户
        update_data = command.model_dump(exclude_unset=True)
        del update_data["user_id"]

        user = await self._domain_service.update_user(command.user_id, update_data)

        if command.company_id is not None:
            # 发布公司变更事件
            event = UserCompanyChangedEvent(
                user_id=user.id,
                old_company_id=user.company.id,
                new_company_id=command.company_id
            )
            await self._event_bus.publish(event)

        return user

    async def change_user_company(self, command: ChangeUserCompanyCommand) -> UserAggregate:
        # 通过领域服务更改公司
        user = await self._domain_service.change_user_company(
            command.user_id,
            command.new_company_id
        )

        # 发布事件
        event = UserCompanyChangedEvent(
            user_id=user.id,
            old_company_id=user.company.id,
            new_company_id=command.new_company_id
        )
        await self._event_bus.publish(event)

        return user

    async def delete_user(self, user_id: int) -> bool:
        return await self._domain_service.delete_user(user_id)
