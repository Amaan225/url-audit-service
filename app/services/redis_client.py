import redis.asyncio as redis

from app.core.config import settings


class RedisClient:
    def __init__(self):

        if settings.REDIS_URL:
            self.client = redis.from_url(
                settings.REDIS_URL,
                decode_responses=True,
            )
        else:
            self.client = redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=0,
                decode_responses=True,
            )

    async def ping(self):
        return await self.client.ping()


_redis_client = None


def get_redis_client():
    global _redis_client

    if _redis_client is None:
        _redis_client = RedisClient()

    return _redis_client