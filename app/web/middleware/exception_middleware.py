from fastapi.responses import ORJSONResponse
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.core.exception import BaseApplicationError
from app.core.vresponse import VResponse


async def error_handler(
    request: Request, exc: BaseApplicationError
) -> JSONResponse:
    return ORJSONResponse(
        status_code=exc.http_code(),
        content=VResponse.fail(
            code=exc.http_code(),
            message=str(exc),
        ).model_dump(),
    )
