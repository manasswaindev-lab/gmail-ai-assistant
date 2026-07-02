
from app.knowledge.matcher import DocumentMatcher
from app.knowledge.repository import KnowledgeRepository
from app.knowledge.models import KnowledgeResult


class KnowledgeService:

    def __init__(self):
        self.repository = KnowledgeRepository()

    def resolve(self, body: str) -> KnowledgeResult:

        documents = self.repository.get_documents()

        matched = DocumentMatcher.match(
            body=body,
            documents=documents,
        )

        return KnowledgeResult(
            documents=matched,
            attachments=[
                str(doc.path)
                for doc in matched
                if doc.path.exists()
            ],
            urls=[
                doc.url
                for doc in matched
            ],
            context=self.build_context(matched),
        )

    @staticmethod
    def build_context(documents) -> str:

        if not documents:
            return ""

        text = "\nAvailable Company Documents\n\n"

        for doc in documents:
            text += f"""
Document:
{doc.name}

Description:
{doc.description}

Download:
{doc.url}

Attachment:
{doc.file_name}

"""

        return text
