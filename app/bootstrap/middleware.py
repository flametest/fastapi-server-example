from fastapi import FastAPI
from app.infrastructure.middleware.logging import LoggingMiddleware

def init_middleware(app: FastAPI) -> None:
    app.add_middleware(LoggingMiddleware)