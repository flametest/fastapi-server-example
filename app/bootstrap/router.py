from fastapi import FastAPI
from app.interfaces.api.v1 import user_router, auth_router

def init_routers(app: FastAPI) -> None:
    app.include_router(router=api_router, prefix=settings.API_PREFIX)
