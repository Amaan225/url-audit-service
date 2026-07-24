from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

from app.services.rate_limit_service import rate_limit_service


class RateLimitMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        if request.method != "POST" or request.url.path != "/audit":
         return await call_next(request)

        client_ip = request.client.host

        key = f"rate_limit:{client_ip}:{request.method}:{request.url.path}"

        allowed = await rate_limit_service.allow_request(key)

        if not allowed:

            return JSONResponse(
                status_code=429,
                content={
    "success": False,
    "retry_after_seconds": 60,
    "error": {
        "code": "RATE_LIMIT_EXCEEDED",
        "message": "Too many requests. Please try again later."
    }
},
            )

        return await call_next(request)