from fastapi.testclient import TestClient
from unittest.mock import AsyncMock

from app.main import app


def test_rate_limit(mocker):

    mocker.patch(
        "app.middleware.rate_limit.rate_limit_service.allow_request",
        new=AsyncMock(
            return_value={
                "allowed": False,
                "remaining": 0,
                "retry_after": 60,
            }
        ),
    )

    with TestClient(app) as client:

        response = client.post(
            "/audit",
            json={
                "url": "https://google.com"
            }
        )

    assert response.status_code == 429

    assert response.headers["Retry-After"] == "60"