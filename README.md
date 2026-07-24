# URL Audit Service

A production-ready URL auditing API built with FastAPI that analyzes websites and returns metadata such as response time, redirects, security headers, content type, and page title. The service includes Redis caching, rate limiting, concurrency control, Docker support, and cloud deployment.

---

## Live Demo

**API:**  
<PASTE_YOUR_RENDER_URL_HERE>

**Swagger Docs:**  
<PASTE_YOUR_RENDER_URL_HERE>/docs

---

## Features

- URL validation
- Async website inspection using httpx
- Redis caching with configurable TTL
- Redis-backed rate limiting
- Concurrency limiting using asyncio.Semaphore
- Structured request logging
- Unique request IDs
- Automatic redirect handling
- Security header inspection
- Docker & Docker Compose support
- Cloud deployment on Render

---

## Tech Stack

- FastAPI
- Python 3.12+
- Redis
- httpx
- Docker
- Uvicorn

---

## API

### POST /audit

Request

```json
{
  "url": "https://google.com"
}
```

Response

```json
{
  "request_id": "...",
  "url": "https://google.com",
  "final_url": "https://www.google.com/",
  "status_code": 200,
  "response_time_ms": 312.5,
  "title": "Google",
  "content_type": "text/html",
  "cached": false
}
```

---

## Local Setup

Clone the repository

```bash
git clone https://github.com/Amaan225/url-audit-service.git
cd url-audit-service
```

Create virtual environment

```bash
python -m venv .venv
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Redis

```bash
docker run -d --name redis-url-audit -p 6379:6379 redis:7-alpine
```

Start the API

```bash
uvicorn app.main:app --reload
```

Open

```
http://localhost:8000/docs
```

---

## Docker

Run

```bash
docker compose up --build
```

---

## Project Structure

```
app/
 ├── api/
 ├── core/
 ├── middleware/
 ├── models/
 ├── services/
 └── main.py

tests/

Dockerfile

docker-compose.yml

requirements.txt
```

---

## Production Features

- Async HTTP requests
- Configurable cache TTL
- Configurable rate limits
- Structured logging
- Request IDs
- Dockerized deployment
- Redis integration

---

## Future Improvements

- Background task queue
- SSL certificate analysis
- Performance score
- Lighthouse integration
- Prometheus metrics
- Grafana dashboards

---

Built for the Digital Heroes Software Development Assessment.

---

Built for **Digital Heroes Training Task**

https://digitalheroes.co