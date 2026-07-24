import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

    CACHE_TTL = int(os.getenv("CACHE_TTL", "300"))

    MAX_CONCURRENT_AUDITS = int(
        os.getenv("MAX_CONCURRENT_AUDITS", "20")
    )

    RATE_LIMIT = int(os.getenv("RATE_LIMIT", "20"))
    RATE_LIMIT_WINDOW = int(
        os.getenv("RATE_LIMIT_WINDOW", "60")
    )


settings = Settings()