import json

from app.ai.client import OpenAIClient
from app.ai.models import EmailAnalysis, ReplyResponse
from app.ai.prompt_builder import PromptBuilder
from app.core.config import settings


class AIService:

    def __init__(self):
        self.client = OpenAIClient().get_client()

    def analyze_email(
        self,
        subject: str,
        sender: str,
        body: str,
    ) -> EmailAnalysis:

        prompt = PromptBuilder.build_analysis_prompt(
            subject=subject,
            sender=sender,
            body=body,
        )

        response = self.client.responses.create(
            model=settings.OPENAI_MODEL,
            input=prompt,
        )

        text = response.output_text.strip()

        try:
            return EmailAnalysis.model_validate_json(text)
        except Exception:
            return EmailAnalysis(**json.loads(text))

    def generate_reply(
        self,
        subject: str,
        sender: str,
        body: str,
        tone: str = "professional",
    ) -> ReplyResponse:

        prompt = PromptBuilder.build_reply_prompt(
            subject=subject,
            sender=sender,
            body=body,
            tone=tone,
        )

        response = self.client.responses.create(
            model=settings.OPENAI_MODEL,
            input=prompt,
        )

        return ReplyResponse(
            reply=response.output_text.strip()
        )