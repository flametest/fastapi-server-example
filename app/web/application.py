from fastapi import FastAPI

from app.core.exception import BaseApplicationError
from app.web.middleware.exception_middleware import error_handler


def setup_middlewares(app: FastAPI) -> None:
    app.add_exception_handler(
        BaseApplicationError,
        error_handler,  # type: ignore
    )
