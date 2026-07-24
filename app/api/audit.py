from fastapi import APIRouter

from app.models.audit import AuditRequest
from app.services.audit_service import audit_service

router = APIRouter(prefix="/audit", tags=["Audit"])


@router.post("")
async def audit_url(request: AuditRequest):
    return await audit_service.audit(str(request.url))