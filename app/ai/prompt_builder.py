from app.ai.prompts import (
    EMAIL_ANALYSIS_PROMPT,
    EMAIL_REPLY_PROMPT,
)


class PromptBuilder:
    """
    Responsible only for building prompts.

    No OpenAI calls.
    No parsing.
    No business logic.
    """

    @staticmethod
    def build_analysis_prompt(
        subject: str,
        sender: str,
        body: str,
    ) -> str:

        return EMAIL_ANALYSIS_PROMPT.format(
            subject=subject,
            sender=sender,
            body=body,
        )

    @staticmethod
    def build_reply_prompt(
        subject: str,
        sender: str,
        body: str,
        tone: str = "professional",
    ) -> str:

        return EMAIL_REPLY_PROMPT.format(
            tone=tone,
            subject=subject,
            sender=sender,
            body=body,
        )