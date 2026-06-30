from fastapi import APIRouter

from app.api.routes.auth import router as auth_router
from app.api.routes.gmail import router as gmail_router
from app.api.routes.health import router as health_router
from app.api.routes.ai import router as ai_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth_router)
api_router.include_router(gmail_router)
api_router.include_router(health_router)
api_router.include_router(ai_router)