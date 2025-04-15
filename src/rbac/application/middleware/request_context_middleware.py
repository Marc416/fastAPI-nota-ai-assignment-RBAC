from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from .context import request_context


class RequestContextMiddleware(BaseHTTPMiddleware):
    """
    데코레이터에서 request를 사용하기 위해 contextvars를 사용하여 request를 저장하는 미들웨어입니다.
    """

    async def dispatch(self, request: Request, call_next):
        token = request_context.set(request)
        try:
            response = await call_next(request)
        finally:
            request_context.reset(token)
        return response
