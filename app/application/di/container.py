from dependency_injector import containers, providers

from app.config import settings
from app.infrastructure.persistence.databases.session import DatabaseSession
from app.application.di.providers.user_container import UserContainer


# 后续可以导入更多的子容器


class AppContainer(containers.DeclarativeContainer):
    """应用主容器"""

    # 配置
    config = providers.Configuration(
        default={
            "db": {
                "url": settings.DATABASE_URL
            }
        }
    )

    # 数据库
    db = providers.Singleton(
        DatabaseSession,
        db_url=config.db.url
    )

    # 用户模块容器
    user_container = providers.Container(
        UserContainer,
        db_engine=db.provided
    )

    # 这里可以添加更多的子容器
    # contact_container = providers.Container(ContactContainer, db_engine=db)
    # order_container = providers.Container(OrderContainer, db_engine=db)
