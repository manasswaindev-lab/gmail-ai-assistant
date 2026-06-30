from google_auth_oauthlib.flow import Flow

CLIENT_SECRET_FILE = "credentials/client_secret.json"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

REDIRECT_URI = "http://localhost:8000/api/v1/auth/callback"


def create_flow(state=None):

    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE,
        scopes=SCOPES,
        state=state
    )

    flow.redirect_uri = REDIRECT_URI

    return flow