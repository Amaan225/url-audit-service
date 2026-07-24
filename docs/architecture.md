# URL Audit Service - Architecture

## Overview

The URL Audit Service is an asynchronous FastAPI application that inspects websites and returns metadata such as response status, redirects, response time, content type, page title, and selected security headers.

The service is designed with production-oriented features including Redis caching, rate limiting, concurrency control, Docker containerization, and cloud deployment.

---

# High-Level Architecture

```
                Client
                   │
                   ▼
          FastAPI Application
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
Rate Limit Middleware   Logging Middleware
        │
        ▼
     /audit Endpoint
        │
        ▼
 Cache Service (Redis)
        │
   Cache Hit? ───────► Return Cached Response
        │
        ▼
Concurrency Controller
        │
        ▼
 Website Inspector
        │
        ▼
    External Website
        │
        ▼
Store Result in Redis
        │
        ▼
Return JSON Response
```

---

# Components

## FastAPI

Handles routing, validation, dependency management, and automatic OpenAPI documentation.

---

## Redis Cache

Audit results are cached for a configurable TTL.

Benefits:

- Faster repeated requests
- Reduced external HTTP traffic
- Lower latency

---

## Rate Limiter

Each client IP is limited to a configurable number of requests per minute.

Benefits:

- Prevents abuse
- Protects infrastructure
- Reduces accidental overload

---

## Concurrency Controller

Implemented using `asyncio.Semaphore`.

Purpose:

- Prevent too many simultaneous outbound HTTP requests
- Keep memory usage predictable
- Improve service stability

---

## Website Inspector

Responsible for:

- Making asynchronous HTTP requests
- Measuring response time
- Following redirects
- Extracting metadata
- Returning normalized audit results

---

## Logging

Each request includes:

- Request ID
- HTTP Method
- Path
- Status Code
- Processing Time

Logs simplify debugging and monitoring.

---

# Request Flow

1. Client sends POST /audit
2. Middleware checks rate limits.
3. Request reaches endpoint.
4. Redis cache is checked.
5. Cache hit returns stored result.
6. Cache miss acquires semaphore.
7. HTTP request is sent.
8. Metadata is extracted.
9. Result stored in Redis.
10. Response returned to client.

---

# Scaling to 10,000 Audits per Day

Current architecture supports horizontal scaling.

Recommended improvements:

- Multiple FastAPI instances
- Shared Redis cluster
- Load Balancer
- Background task queue (Celery/RQ)
- Prometheus monitoring
- Grafana dashboards

---

# Failure Handling

Current implementation handles:

- Invalid URLs
- Connection errors
- Timeouts
- Redis cache misses
- Rate limit violations

Future improvements:

- Circuit breaker
- Retry strategy
- Dead letter queue

---

# Monitoring

Recommended metrics:

- Average response time
- Cache hit ratio
- Error rate
- Request volume
- Redis latency
- External request latency

---

# Technology Choices

| Technology | Reason |
|------------|--------|
| FastAPI | High-performance asynchronous framework |
| Redis | Fast in-memory caching and rate limiting |
| Docker | Reproducible deployments |
| httpx | Async HTTP client |
| Uvicorn | ASGI server |

---

# Trade-offs

Advantages:

- Fast responses
- Low latency
- Production-ready architecture
- Easy deployment

Limitations:

- Redis dependency
- Single service architecture
- No background processing
- Limited monitoring

---

# Future Enhancements

- SSL certificate analysis
- Lighthouse integration
- Queue-based architecture
- Prometheus metrics
- Grafana dashboards
- Kubernetes deployment