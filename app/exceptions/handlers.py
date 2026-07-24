from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(httpx.TimeoutException)
    async def timeout_handler(request: Request, exc: httpx.TimeoutException):
        return JSONResponse(
            status_code=504,
            content={
                "success": False,
                "error": {
                    "code": "TIMEOUT",
                    "message": "Target server did not respond within timeout."
                }
            },
        )

    @app.exception_handler(httpx.ConnectError)
    async def connect_handler(request: Request, exc: httpx.ConnectError):
        return JSONResponse(
            status_code=502,
            content={
                "success": False,
                "error": {
                    "code": "CONNECTION_ERROR",
                    "message": "Unable to connect to target website."
                }
            },
        )

    @app.exception_handler(Exception)
    async def generic_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": {
                    "code": "INTERNAL_SERVER_ERROR",
                    "message": "Unexpected server error."
                }
            },
        )