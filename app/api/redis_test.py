from fastapi import APIRouter

from app.services.redis_client import redis_client

router = APIRouter(prefix="/redis", tags=["Redis"])


@router.get("/ping")
async def ping():

    result = await redis_client.ping()

    return {
        "redis": result
    }