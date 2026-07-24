import time
from datetime import datetime, UTC
from uuid import uuid4

import httpx
from bs4 import BeautifulSoup


class WebsiteInspector:

    TIMEOUT = 10

    async def inspect(self, url: str):

        request_id = str(uuid4())

        start = time.perf_counter()

        async with httpx.AsyncClient(
            follow_redirects=True,
            timeout=self.TIMEOUT,
        ) as client:

            response = await client.get(url)

        end = time.perf_counter()

        response_time = round((end - start) * 1000, 2)

        title = None

        if "text/html" in response.headers.get("content-type", ""):
            soup = BeautifulSoup(response.text, "lxml")

            if soup.title:
                title = soup.title.text.strip()

        content_length = response.headers.get("content-length")

        if content_length is None:
            content_length = len(response.content)

        security_headers = {
            "strict_transport_security": "strict-transport-security"
            in response.headers,
            "content_security_policy": "content-security-policy"
            in response.headers,
            "x_frame_options": "x-frame-options"
            in response.headers,
            "x_content_type_options": "x-content-type-options"
            in response.headers,
        }

        return {
            "request_id": request_id,
            "url": url,
            "final_url": str(response.url),
            "status_code": response.status_code,
            "response_time_ms": response_time,
            "title": title,
            "content_type": response.headers.get("content-type"),
            "content_length": int(content_length),
            "server": response.headers.get("server"),
            "https": str(response.url).startswith("https"),
            "redirects": len(response.history),
            "security_headers": security_headers,
            "cached": False,
            "timestamp": datetime.now(UTC).isoformat(),
        }


website_inspector = WebsiteInspector()