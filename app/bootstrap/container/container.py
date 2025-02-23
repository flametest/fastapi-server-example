from dependency_injector import containers, providers

from app.application.event_bus.event_bus import EventBus
from app.bootstrap.container.providers.user_container import UserContainer
from app.config import settings
from app.infrastructure.database.session import DatabaseSession
from app.infrastructure.persistence.unit_of_work import UnitOfWork


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

    # 工作单元
    unit_of_work = providers.Factory(
        UnitOfWork,
        session=db.provided.session,
    )

    # 用户模块容器
    user_container = providers.Container(
        UserContainer,
        db_engine=db.provided,
        event_bus=event_bus.provided,
        unit_of_work=unit_of_work.provided,
    )

    # 这里可以添加更多的子容器
    # contact_container = providers.Container(ContactContainer, db_engine=db)
    # order_container = providers.Container(OrderContainer, db_engine=db)
