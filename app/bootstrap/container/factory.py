from app.bootstrap.container.container import AppContainer
from app.infrastructure.config import settings


def create_container() -> AppContainer:
    container = AppContainer()

    # 加载配置
    container.config.from_dict({
        "db": {
            "url": settings.DATABASE_URL,
        }
    })

    return container
