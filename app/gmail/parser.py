import base64
from typing import Any


class GmailParser:
    """
    Converts raw Gmail API messages into simple Python dictionaries.
    """

    @staticmethod
    def parse_message(message: dict[str, Any]) -> dict[str, Any]:

        payload = message.get("payload", {})
        headers = payload.get("headers", [])

        return {
            "id": message.get("id"),
            "thread_id": message.get("threadId"),
            "history_id": message.get("historyId"),
            "internal_date": message.get("internalDate"),
            "label_ids": message.get("labelIds", []),
            "snippet": message.get("snippet", ""),
            "subject": GmailParser.get_header(headers, "Subject"),
            "from": GmailParser.get_header(headers, "From"),
            "to": GmailParser.get_header(headers, "To"),
            "cc": GmailParser.get_header(headers, "Cc"),
            "bcc": GmailParser.get_header(headers, "Bcc"),
            "reply_to": GmailParser.get_header(headers, "Reply-To"),
            "date": GmailParser.get_header(headers, "Date"),
            "body": GmailParser.extract_body(payload),
        }

    @staticmethod
    def get_header(headers: list[dict], name: str) -> str | None:

        for header in headers:
            if header.get("name", "").lower() == name.lower():
                return header.get("value")

        return None

    @staticmethod
    def extract_body(payload: dict) -> str:
        """
        Returns the plain-text body if available.
        Falls back to HTML if plain text is unavailable.
        """

        # Single-part message
        body = payload.get("body", {})
        data = body.get("data")

        if data:
            return GmailParser.decode_base64(data)

        # Multipart message
        return GmailParser.extract_parts(payload.get("parts", []))

    @staticmethod
    def extract_parts(parts: list[dict]) -> str:

        html_body = ""

        for part in parts:

            mime = part.get("mimeType", "")

            # Plain text preferred
            if mime == "text/plain":

                data = part.get("body", {}).get("data")

                if data:
                    return GmailParser.decode_base64(data)

            # Save HTML as fallback
            if mime == "text/html":

                data = part.get("body", {}).get("data")

                if data:
                    html_body = GmailParser.decode_base64(data)

            # Nested MIME messages
            if part.get("parts"):

                nested = GmailParser.extract_parts(part["parts"])

                if nested:
                    return nested

        return html_body

    @staticmethod
    def decode_base64(data: str) -> str:

        try:

            padding = "=" * (-len(data) % 4)

            decoded = base64.urlsafe_b64decode(data + padding)

            return decoded.decode("utf-8", errors="ignore")

        except Exception:

            return ""