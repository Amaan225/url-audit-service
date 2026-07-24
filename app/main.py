from fastapi import FastAPI
from app.exceptions.handlers import register_exception_handlers
from app.api.audit import router as audit_router
from app.middleware.request_id import RequestIDMiddleware
from app.api.redis_test import router as redis_router
from app.api.cache_test import router as cache_router
from app.middleware.rate_limit import RateLimitMiddleware
from app.core.logging_config import setup_logging
from app.middleware.logging import LoggingMiddleware

setup_logging()

app = FastAPI(
    title="URL Audit Service",
    description="Production-grade URL Audit Service",
    version="1.0.0",
)
register_exception_handlers(app)
app.add_middleware(RequestIDMiddleware)
app.add_middleware(RateLimitMiddleware)
app.include_router(audit_router)
app.add_middleware(LoggingMiddleware)

app.include_router(audit_router)
app.include_router(redis_router)
app.include_router(cache_router)

@app.get("/")
async def root():
    return {
        "message": "URL Audit Service is running 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }