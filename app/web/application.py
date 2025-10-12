from fastapi import FastAPI

from app.core.exception import BaseApplicationError
from app.web.middleware.exception_middleware import error_handler
from app.web.middleware.logging_middleware import LoggingMiddleware


def setup_middlewares(app: FastAPI) -> None:
    app.add_exception_handler(
        BaseApplicationError,
        error_handler,  # type: ignore
    )
    app.add_middleware(LoggingMiddleware)
