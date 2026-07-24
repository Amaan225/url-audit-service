from app.services.cache_service import cache_service
from app.services.website_inspector import website_inspector
from app.services.concurrency_service import concurrency_service


class AuditService:

    async def audit(self, url: str):

        cache_key = f"audit:{url.lower().rstrip('/')}"

        cached = await cache_service.get(cache_key)

        if cached is not None:

            cached["cached"] = True

            ttl = await cache_service.ttl(cache_key)

            cached["cache"] = {
                "hit": True,
                "ttl_remaining": ttl,
            }

            return cached

        async with concurrency_service.semaphore:
            result = await website_inspector.inspect(url)
        result["cached"] = False

        result["cache"] = {
            "hit": False,
            "ttl_remaining": 300,
        }

        await cache_service.set(
            cache_key,
            result,
        )

        return result


audit_service = AuditService()