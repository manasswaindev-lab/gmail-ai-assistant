from email.message import EmailMessage
from pathlib import Path
import mimetypes
import base64

from googleapiclient.discovery import Resource


class GmailSendService:

    def __init__(self, gmail_service: Resource):

        self.gmail = gmail_service

    def send_email(
        self,
        to: str,
        subject: str,
        body: str,
        attachments: list[str] | None = None,
    ):

        message = EmailMessage()

        message["To"] = to

        message["Subject"] = subject

        message.set_content(body)

        attachments = attachments or []

        for file_path in attachments:

            path = Path(file_path)

            if not path.exists():
                continue

            mime_type, _ = mimetypes.guess_type(path)

            if mime_type:
                maintype, subtype = mime_type.split("/")
            else:
                maintype = "application"
                subtype = "octet-stream"

            with open(path, "rb") as f:

                message.add_attachment(
                    f.read(),
                    maintype=maintype,
                    subtype=subtype,
                    filename=path.name,
                )

        encoded = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode()

        self.gmail.users().messages().send(
            userId="me",
            body={
                "raw": encoded
            },
        ).execute()