import asyncio

import fastapi
import uvicorn

from app.config import settings
from app.bootstrap.startup import bootstrap_app

app: fastapi.FastAPI = asyncio.run(bootstrap_app())

if __name__ == '__main__':
    uvicorn.run(
        app="app.main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        log_level=settings.LOGGING_LEVEL,
        # reload=True,
    )
