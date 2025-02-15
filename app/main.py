import fastapi
import uvicorn

from app.config import settings
from app.interfaces.api import router as api_router


def init_app() -> fastapi.FastAPI:
    app = fastapi.FastAPI()
    app.include_router(router=api_router, prefix=settings.API_PREFIX)
    return app


app: fastapi.FastAPI = init_app()

if __name__ == '__main__':
    uvicorn.run(
        app="app.main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        log_level=settings.LOGGING_LEVEL,
        # reload=True,
    )
