# Failure Mode Analysis

## 1. External Website Timeout

### Impact

Audit requests become slow or fail.

### Mitigation

- Configured request timeout
- Structured error responses
- Asynchronous processing prevents blocking other requests

---

## 2. Redis Unavailable

### Impact

Caching and rate limiting become unavailable.

### Mitigation

The application can continue performing direct URL inspections. Cache misses simply result in fresh inspections.

Future improvement:

- Graceful degradation mode
- Redis health monitoring

---

## 3. Traffic Spike

### Impact

Too many concurrent requests could exhaust resources.

### Mitigation

- asyncio.Semaphore limits concurrent inspections.
- Redis-backed rate limiting prevents abuse.
- Horizontal scaling can distribute requests across multiple instances.