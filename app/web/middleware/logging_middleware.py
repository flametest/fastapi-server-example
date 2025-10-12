import json
import logging
from http import HTTPMethod

from starlette.datastructures import FormData
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        path = request.url.path
        method = request.method
        params = request.query_params
        body: str | None = None

        if (
            method == HTTPMethod.POST
            and request.headers.get("content-type") == "application/json"
        ):
            body_dict = await request.json()
            body = json.dumps(body_dict)
            request._body = body.encode("utf-8")

        elif (
            method == HTTPMethod.POST
            and request.headers.get("content-type")
            == "application/x-www-form-urlencoded"
        ):
            form = await request.form()
            if isinstance(form, FormData):
                body = "&".join([f"{k}={v}" for k, v in form.multi_items()])
                request._body = body.encode("utf-8")

        logger.info(f"Request: {method} {path} {params} body: {body}")
        return await call_next(request)
