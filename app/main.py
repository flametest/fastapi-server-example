import fastapi
import uvicorn

from app.config import settings
from app.core.logging import setup_logging
from app.web.api import router as api_router
from app.web.application import setup_middlewares


def init_app() -> fastapi.FastAPI:
    app = fastapi.FastAPI()
    app.include_router(router=api_router, prefix=settings.API_PREFIX)
    setup_middlewares(app)
    setup_logging()
    return app


if __name__ == "__main__":
    uvicorn.run(
        app="app.main:init_app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        log_level=settings.LOGGING_LEVEL,
        reload=True,
    )
