from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.services.rate_limit_service import rate_limit_service


class RateLimitMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        # Only rate limit POST /audit
        if request.method != "POST" or request.url.path != "/audit":
            return await call_next(request)

        client_ip = request.client.host
        key = f"rate_limit:{client_ip}:{request.method}:{request.url.path}"

        result = await rate_limit_service.allow_request(key)

        if not result["allowed"]:
            return JSONResponse(
                status_code=429,
                content={
                    "success": False,
                    "retry_after_seconds": result["retry_after"],
                    "error": {
                        "code": "RATE_LIMIT_EXCEEDED",
                        "message": "Too many requests. Please try again later."
                    }
                },
                headers={
                    "Retry-After": str(result["retry_after"]),
                    "X-RateLimit-Limit": str(rate_limit_service.LIMIT),
                    "X-RateLimit-Remaining": "0",
                },
            )

        response = await call_next(request)

        response.headers["X-RateLimit-Limit"] = str(rate_limit_service.LIMIT)
        response.headers["X-RateLimit-Remaining"] = str(result["remaining"])

        return response