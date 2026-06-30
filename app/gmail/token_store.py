from google.oauth2.credentials import Credentials


class TokenStore:
    """
    Temporary in-memory token storage.

    Replace this later with Redis or PostgreSQL.
    """

    credentials: Credentials | None = None