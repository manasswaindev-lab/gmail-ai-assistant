from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app.gmail.oauth import create_flow
from app.gmail.token_store import TokenStore

router = APIRouter(tags=["Authentication"])


@router.get("/login")
def login(request: Request):
    """
    Redirect user to Google OAuth login.
    """

    flow = create_flow()

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent",
    )

    # Save OAuth state
    request.session["state"] = state

    # Save PKCE verifier
    request.session["code_verifier"] = flow.code_verifier

    return RedirectResponse(url=authorization_url)


@router.get("/auth/callback")
def auth_callback(request: Request):
    """
    Google redirects here after successful login.
    """

    state = request.session.get("state")
    code_verifier = request.session.get("code_verifier")

    if not state or not code_verifier:
        return {
            "error": "OAuth session expired. Please login again."
        }

    # Recreate the same OAuth flow
    flow = create_flow(state=state)
    flow.code_verifier = code_verifier

    # Exchange authorization code for access token
    flow.fetch_token(
        authorization_response=str(request.url)
    )

    credentials = flow.credentials

    # Store credentials in memory
    TokenStore.credentials = credentials

    print("=" * 60)
    print("Google Login Successful")
    print("Access Token Saved")
    print("Refresh Token :", credentials.refresh_token)
    print("=" * 60)

    return RedirectResponse(
        url="/api/v1/gmail/messages?max_results=10"
    )