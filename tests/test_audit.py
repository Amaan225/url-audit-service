from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import AsyncMock


def allow(*args, **kwargs):
    return {
        "allowed": True,
        "remaining": 19,
        "retry_after": 60,
    }


def test_invalid_url(mocker):
    mocker.patch(
        "app.services.rate_limit_service.rate_limit_service.allow_request",
        new=AsyncMock(
            return_value={
                "allowed": True,
                "remaining": 19,
                "retry_after": 60,
            }
        ),
    )

    with TestClient(app) as client:
        response = client.post(
            "/audit",
            json={"url": "not-a-url"},
        )

    assert response.status_code == 422


def test_missing_url(mocker):

    mocker.patch(
        "app.middleware.rate_limit.rate_limit_service.allow_request",
        new=AsyncMock(
            return_value={
                "allowed": True,
                "remaining": 19,
                "retry_after": 60,
            }
        ),
    )

    with TestClient(app) as client:

        response = client.post(
            "/audit",
            json={}
        )

    assert response.status_code == 422


def test_valid_url(mocker):
    mocker.patch(
        "app.services.rate_limit_service.rate_limit_service.allow_request",
        new=AsyncMock(
            return_value={
                "allowed": True,
                "remaining": 19,
                "retry_after": 60,
            }
        ),
    )

    with TestClient(app) as client:
        response = client.post(
            "/audit",
            json={"url": "https://google.com"},
        )

    assert response.status_code == 200

    body = response.json()

    assert "request_id" in body
    assert "status_code" in body
    assert "response_time_ms" in body