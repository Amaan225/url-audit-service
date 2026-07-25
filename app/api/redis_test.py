from fastapi import APIRouter
from app.services.redis_client import get_redis_client

router = APIRouter(prefix="/redis", tags=["Redis"])


@router.get("/ping")
async def ping():

    result = await get_redis_client().ping()

    return {
        "redis": result
    }