from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


class GmailClient:
    """
    Wrapper around the Gmail REST API.
    Responsible only for communicating with Gmail.
    """

    def __init__(self, credentials: Credentials):
        self.service = build(
            serviceName="gmail",
            version="v1",
            credentials=credentials
        )

    def list_messages(self, max_results: int = 10):
        """
        Returns a list of message metadata.
        """

        return (
            self.service.users()
            .messages()
            .list(
                userId="me",
                maxResults=max_results
            )
            .execute()
        )

    def get_message(self, message_id: str):
        """
        Returns a complete Gmail message.
        """

        return (
            self.service.users()
            .messages()
            .get(
                userId="me",
                id=message_id,
                format="full"
            )
            .execute()
        )

    def list_labels(self):
        """
        Returns all Gmail labels.
        """

        return (
            self.service.users()
            .labels()
            .list(
                userId="me"
            )
            .execute()
        )

    def search_messages(
        self,
        query: str,
        max_results: int = 10
    ):
        """
        Search Gmail using Gmail search syntax.

        Examples:
            from:amazon
            is:unread
            newer_than:7d
        """

        return (
            self.service.users()
            .messages()
            .list(
                userId="me",
                q=query,
                maxResults=max_results
            )
            .execute()
        )