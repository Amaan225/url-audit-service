from app.services.cache_service import cache_service
from app.services.website_inspector import website_inspector
from app.services.concurrency_service import concurrency_service
import time
from copy import deepcopy


class AuditService:

    async def audit(self, url: str):

        api_start = time.perf_counter()

        cache_key = f"audit:{url.lower().rstrip('/')}"

        cached = await cache_service.get(cache_key)

        if cached is not None:

            result = deepcopy(cached)

            result["cached"] = True

            ttl = await cache_service.ttl(cache_key)

            result["cache"] = {
                "hit": True,
                "ttl_remaining": ttl,
            }

            api_end = time.perf_counter()

            result["api_response_time_ms"] = round(
                (api_end - api_start) * 1000,
                2,
            )

            return result

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

        api_end = time.perf_counter()

        result["api_response_time_ms"] = round(
            (api_end - api_start) * 1000,
            2,
        )

        return result

audit_service = AuditService()