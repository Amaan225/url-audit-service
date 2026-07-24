# Observability and Rollback Plan

# Monitoring

The following metrics should be monitored:

- Request latency
- Cache hit ratio
- Redis availability
- HTTP error rate
- Request volume
- Average response time
- Rate limit violations

---

# Alerting

Alerts should trigger when:

- Redis becomes unavailable
- Error rate exceeds 5%
- Average latency exceeds 2 seconds
- Cache hit ratio drops significantly
- Service health checks fail

---

# Rollback Strategy

Deployment should follow a rolling deployment strategy.

If a deployment introduces failures:

1. Stop routing traffic to the new version.
2. Redeploy the previous stable Docker image.
3. Verify health checks.
4. Restore traffic.

Because deployments are containerized, rollback only requires redeploying the previous image.

---

# Future Improvements

- Prometheus
- Grafana
- OpenTelemetry
- Distributed tracing
- Centralized log aggregation