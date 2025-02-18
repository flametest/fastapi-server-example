from dependency_injector import containers, providers

from app.application.commands.handlers.user_commands import UserCommands
from app.application.queries.user_queries import UserQueries
from app.application.services.user_service import UserApplicationService
from app.domain.services.user_service import UserService
from app.infrastructure.persistence.repository.company_repository import CompanyRepository
from app.infrastructure.persistence.repository.user_repository import UserRepository


class UserContainer(containers.DeclarativeContainer):
    """联系人模块容器"""

    # 依赖通用容器的数据库配置
    db_engine = providers.Dependency()
    event_bus = providers.Dependency()

    # 仓储层
    user_repository = providers.Singleton(
        UserRepository,
        engine=db_engine
    )
    company_repository = providers.Singleton(
        CompanyRepository,
        engine=db_engine
    )
    # 服务层
    user_domain_service = providers.Singleton(
        UserService,
        user_repository=user_repository,
        company_repository=CompanyRepository
    )

    # 用户服务
    user_service = providers.Factory(
        UserApplicationService,
        domain_service=user_domain_service,
        event_bus=event_bus
    )

    # 命令服务
    user_commands = providers.Factory(
        UserCommands,
        user_service=user_service,
    )

    # 查询服务
    user_queries = providers.Factory(
        UserQueries,
        user_repository=user_repository
    )
