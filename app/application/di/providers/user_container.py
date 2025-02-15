from dependency_injector import containers, providers

from app.infrastructure.repository.user_repository import UserRepository


class ContactContainer(containers.DeclarativeContainer):
    """联系人模块容器"""

    # 依赖通用容器的数据库配置
    db_engine = providers.Dependency()

    # 仓储层
    user_repository = providers.Singleton(
        UserRepository,
        engine=db_engine
    )

    # 服务层
    user_service = providers.Singleton(
        UserService,
        user_repository=user_repository
    )
