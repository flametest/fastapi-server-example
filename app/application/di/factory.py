from app.application.di.container import Container
from app.core.config import settings


def create_container() -> Container:
    container = Container()
    
    # 加载配置
    container.config.from_dict({
        "db": {
            "url": settings.DATABASE_URL,
        }
    })
    
    return container