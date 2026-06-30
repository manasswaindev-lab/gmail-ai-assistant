import os

# Allow HTTP only for local development
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import logger

logger.info("Starting Gmail AI Assistant...")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

# Session Middleware
app.add_middleware(
    SessionMiddleware,
    secret_key="change-this-to-a-random-secret-key"
)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Gmail AI Assistant",
        "version": settings.APP_VERSION
    }