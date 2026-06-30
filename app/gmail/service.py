from google.oauth2.credentials import Credentials

from app.gmail.client import GmailClient
from app.gmail.parser import GmailParser


class GmailService:
    """
    Business layer for Gmail operations.

    Responsibilities:
    - Read emails
    - Search emails
    - Retrieve a single email
    - Convert Gmail API responses into simple Python objects
    """

    def __init__(self, credentials: Credentials):
        self.client = GmailClient(credentials)

    def get_latest_emails(self, max_results: int = 10) -> list[dict]:
        """
        Return the latest emails.
        """

        response = self.client.list_messages(max_results)

        messages = response.get("messages", [])

        parsed_messages = []

        for message in messages:

            raw_message = self.client.get_message(message["id"])

            parsed_messages.append(
                GmailParser.parse_message(raw_message)
            )

        return parsed_messages

    def get_email(self, message_id: str) -> dict:
        """
        Return a single email.
        """

        raw_message = self.client.get_message(message_id)

        return GmailParser.parse_message(raw_message)

    def search_emails(
        self,
        query: str,
        max_results: int = 10
    ) -> list[dict]:
        """
        Search Gmail.

        Example:

        from:amazon

        is:unread

        newer_than:7d
        """

        response = self.client.search_messages(
            query=query,
            max_results=max_results,
        )

        messages = response.get("messages", [])

        results = []

        for message in messages:

            raw_message = self.client.get_message(message["id"])

            results.append(
                GmailParser.parse_message(raw_message)
            )

        return results

    def get_labels(self):
        """
        Return Gmail labels.
        """

        response = self.client.list_labels()

        return response.get("labels", [])