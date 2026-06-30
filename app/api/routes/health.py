from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("")
def health():
    return {
        "status": "UP",
        "application": "gmail-ai-assistant",
        "version": "1.0.0"
    }