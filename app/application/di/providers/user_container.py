from dependency_injector import containers, providers

from app.infrastructure.repository.user_repository import UserRepository
from app.domain.services.user_service import UserService


class UserContainer(containers.DeclarativeContainer):
    """联系人模块容器"""

    # 依赖通用容器的数据库配置
    db_engine = providers.Dependency()

    # 仓储层
    user_repository = providers.Singleton(
        UserRepository,
        engine=db_engine
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

    # 服务层
    user_service = providers.Singleton(
        UserService,
        user_repository=user_repository
    )
