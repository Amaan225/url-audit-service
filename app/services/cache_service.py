import json

from app.services.redis_client import redis_client


class CacheService:

    DEFAULT_TTL = 300

    async def get(self, key: str):

        data = await redis_client.client.get(key)

        if data is None:
            return None

        return json.loads(data)

    async def set(self, key: str, value: dict, ttl: int = DEFAULT_TTL):

        await redis_client.client.set(
            key,
            json.dumps(value),
            ex=ttl,
        )

    async def ttl(self, key: str):

        return await redis_client.client.ttl(key)


cache_service = CacheService()