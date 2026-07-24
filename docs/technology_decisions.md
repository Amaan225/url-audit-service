# Technology Decision Record (TDR)

## Overview

This document records the major technology choices made during the implementation of the URL Audit Service and explains why each technology was selected over alternatives.

---

# 1. Web Framework

## Chosen

FastAPI

## Alternatives Considered

- Flask
- Django REST Framework

## Reason

FastAPI provides native asynchronous support, automatic OpenAPI documentation, request validation through Pydantic, and excellent performance for I/O-bound workloads.

Flask would require additional extensions for validation and async support.

Django REST Framework is more suitable for database-heavy applications than lightweight API services.

---

# 2. Cache

## Chosen

Redis

## Alternatives Considered

- Python dictionary
- Memcached

## Reason

Redis provides:

- TTL support
- Shared cache across instances
- Extremely fast read/write performance

A Python dictionary would only work inside a single process.

---

# 3. HTTP Client

## Chosen

httpx

## Alternatives Considered

- requests
- aiohttp

## Reason

httpx supports asynchronous HTTP requests while maintaining an API similar to requests.

---

# 4. Deployment

## Chosen

Render

## Alternatives Considered

- Railway
- Fly.io

## Reason

Render offers simple deployment, Docker support, free hosting, and managed Redis.

---

# 5. Containerization

## Chosen

Docker

## Alternatives Considered

- Native deployment

## Reason

Docker provides consistent environments across development and production while simplifying deployment.