from fastapi import APIRouter, HTTPException

from app.ai.models import ReplyRequest
from app.ai.service import AIService
from app.gmail.service import GmailService
from app.gmail.token_store import TokenStore

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


def get_gmail_service():

    if TokenStore.credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Please login with Google first."
        )

    return GmailService(TokenStore.credentials)


@router.get("/message/{message_id}")
def analyze_email(message_id: str):

    gmail = get_gmail_service()

    email = gmail.get_email(message_id)

    ai = AIService()

    analysis = ai.analyze_email(
        subject=email["subject"],
        sender=email["from"],
        body=email["body"],
    )

    return {
        "message_id": message_id,
        "subject": email["subject"],
        "from": email["from"],
        "analysis": analysis.model_dump(),
    }


@router.post("/reply/{message_id}")
def generate_reply(
    message_id: str,
    request: ReplyRequest,
):

    gmail = get_gmail_service()

    email = gmail.get_email(message_id)

    ai = AIService()

    reply = ai.generate_reply(
        subject=email["subject"],
        sender=email["from"],
        body=email["body"],
        tone=request.tone,
    )

    return {
        "message_id": message_id,
        "subject": email["subject"],
        "reply": reply.reply,
    }