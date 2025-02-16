from fastapi import FastAPI
from app.bootstrap.container.factory import create_container
from app.bootstrap.middleware import init_middleware
from app.bootstrap.router import init_routers
from app.infrastructure.logging.setup import setup_logging


async def bootstrap_app() -> FastAPI:
    # 初始化应用
    app = FastAPI()

    # 初始化日志
    setup_logging()

    # 初始化容器
    container = create_container()
    app.container = container

    # 初始化中间件
    init_middleware(app)

    # 初始化路由
    init_routers(app)

    return app
