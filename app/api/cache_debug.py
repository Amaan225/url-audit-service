from fastapi import APIRouter

from app.services.cache_service import cache_service

router = APIRouter(prefix="/cache", tags=["Cache"])


@router.get("/test")
async def test():

    await cache_service.set(
        "hello",
        {
            "message": "Redis is working!"
        }
    )

    value = await cache_service.get("hello")

    ttl = await cache_service.ttl("hello")

    return {
        "cached_value": value,
        "ttl": ttl
    }