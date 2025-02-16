import time
import logging
from typing import Callable
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # 记录请求开始时间
        start_time = time.time()
        
        # 记录请求信息
        logger.info(f"Request: {request.method} {request.url}")
        logger.info(f"Client IP: {request.client.host}")
        logger.info(f"Headers: {request.headers}")

        try:
            # 处理请求
            response = await call_next(request)
            
            # 计算处理时间
            process_time = time.time() - start_time
            
            # 记录响应信息
            logger.info(f"Response Status: {response.status_code}")
            logger.info(f"Process Time: {process_time:.3f}s")
            
            return response
            
        except Exception as e:
            # 记录错误信息
            logger.error(f"Request failed: {str(e)}")
            process_time = time.time() - start_time
            logger.error(f"Failed Process Time: {process_time:.3f}s")
            raise