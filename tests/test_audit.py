from fastapi.testclient import TestClient
from app.main import app


def test_invalid_url():
    with TestClient(app) as client:
        response = client.post(
            "/audit",
            json={"url": "not-a-url"},
        )
        assert response.status_code == 422


# def test_missing_url():
#     with TestClient(app) as client:
#         response = client.post(
#             "/audit",
#             json={},
#         )
#         assert response.status_code == 422


def test_valid_url():
    with TestClient(app) as client:
        response = client.post(
            "/audit",
            json={"url": "https://google.com"},
        )

        assert response.status_code == 200

        body = response.json()

        assert "status_code" in body
        assert "response_time_ms" in body
        assert "request_id" in body