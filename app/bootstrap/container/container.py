from dependency_injector import containers, providers

from app.application.event_bus.event_bus import EventBus
from app.bootstrap.container.providers.user_container import UserContainer
from app.config import settings
from app.infrastructure.database.session import DatabaseSession


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

    # 事件总线
    event_bus = providers.Singleton(EventBus)

    # 用户模块容器
    user_container = providers.Container(
        UserContainer,
        db_engine=db.provided
    )

    # 这里可以添加更多的子容器
    # contact_container = providers.Container(ContactContainer, db_engine=db)
    # order_container = providers.Container(OrderContainer, db_engine=db)
