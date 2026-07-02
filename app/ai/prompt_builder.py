from app.ai.prompts import EMAIL_ANALYSIS_PROMPT, EMAIL_REPLY_PROMPT

class PromptBuilder:

    @staticmethod
    def build_analysis_prompt(subject: str, sender: str, body: str) -> str:
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
        knowledge_context: str = "",
    ) -> str:
        prompt = EMAIL_REPLY_PROMPT.format(
            tone=tone,
            subject=subject,
            sender=sender,
            body=body,
        )
        if knowledge_context:
            prompt += f'''

---------------------------------------------------------
Company Knowledge

{knowledge_context}

---------------------------------------------------------
Instructions

If company documents are available:
- Mention them naturally.
- Mention they are attached.
- Mention the download URLs.
- Never invent URLs.
- Never invent documents.
'''
        return prompt
