import asyncio

import fastapi
import uvicorn

from app.config import settings
from app.bootstrap.startup import bootstrap_app

app: fastapi.FastAPI = None


def create_app() -> fastapi.FastAPI:
    import asyncio
    async def init() -> fastapi.FastAPI:
        return await bootstrap_app()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(init())


if __name__ == '__main__':
    uvicorn.run(
        app="app.main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        log_level=settings.LOGGING_LEVEL,
        # reload=True,
    )
