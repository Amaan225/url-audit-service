import asyncio


class ConcurrencyService:

    MAX_CONCURRENT_AUDITS = 20

    def __init__(self):
        self.semaphore = asyncio.Semaphore(
            self.MAX_CONCURRENT_AUDITS
        )


concurrency_service = ConcurrencyService()