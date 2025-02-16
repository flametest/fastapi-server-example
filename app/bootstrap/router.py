from fastapi import FastAPI

from app.config import settings
from app.interfaces.api.v1 import router as api_router


def init_routers(app: FastAPI) -> None:
    app.include_router(router=api_router, prefix=settings.API_PREFIX)
