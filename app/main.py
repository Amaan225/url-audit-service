from fastapi import FastAPI

from app.api.audit import router as audit_router

app = FastAPI(
    title="URL Audit Service",
    description="Production-grade URL Audit Service",
    version="1.0.0",
)

app.include_router(audit_router)


@app.get("/")
async def root():
    return {
        "message": "URL Audit Service is running 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }