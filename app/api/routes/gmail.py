from fastapi import APIRouter, HTTPException, Query

from app.gmail.service import GmailService
from app.gmail.token_store import TokenStore

router = APIRouter(
    prefix="/gmail",
    tags=["Gmail"],
)


def get_service():

    print("Current Credentials:", TokenStore.credentials)

    if TokenStore.credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Please login with Google first."
        )

    return GmailService(TokenStore.credentials)


@router.get("/messages")
def list_messages(
    max_results: int = Query(10, ge=1, le=100)
):
    service = get_service()
    return service.get_latest_emails(max_results)


@router.get("/message/{message_id}")
def get_message(message_id: str):
    service = get_service()
    return service.get_email(message_id)


@router.get("/search")
def search_messages(
    q: str,
    max_results: int = Query(10, ge=1, le=100)
):
    service = get_service()
    return service.search_emails(
        query=q,
        max_results=max_results
    )


@router.get("/labels")
def labels():
    service = get_service()
    return service.get_labels()