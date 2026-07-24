from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict


class AuditRequest(BaseModel):
    url: HttpUrl


class SecurityHeaders(BaseModel):
    strict_transport_security: bool
    content_security_policy: bool
    x_frame_options: bool
    x_content_type_options: bool


class AuditResponse(BaseModel):
    request_id: str
    url: str
    final_url: str
    status_code: int
    response_time_ms: float
    title: Optional[str] = None
    content_type: Optional[str] = None
    content_length: Optional[int] = None
    server: Optional[str] = None
    https: bool
    redirects: int
    security_headers: SecurityHeaders
    cached: bool
    timestamp: str