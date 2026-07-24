import redis.asyncio as redis


class RedisClient:
    def __init__(self):
        self.client = redis.Redis(
            host="localhost",
            port=6379,
            db=0,
            decode_responses=True,
        )

    async def ping(self):
        return await self.client.ping()


redis_client = RedisClient()