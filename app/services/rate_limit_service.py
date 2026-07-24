from app.services.redis_client import redis_client


class RateLimitService:

    LIMIT = 20
    WINDOW = 60

    async def allow_request(self, key: str):

        current = await redis_client.client.incr(key)

        if current == 1:
            await redis_client.client.expire(
                key,
                self.WINDOW,
            )

        ttl = await redis_client.client.ttl(key)

        return {
            "allowed": current <= self.LIMIT,
            "remaining": max(0, self.LIMIT - current),
            "retry_after": ttl,
        }


rate_limit_service = RateLimitService()