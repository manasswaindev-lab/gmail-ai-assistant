from app.knowledge.models import KnowledgeDocument


class DocumentMatcher:

    @staticmethod
    def match(
        body: str,
        documents: list[KnowledgeDocument],
    ) -> list[KnowledgeDocument]:

        body = body.lower()

        matched = []

        for document in documents:

            if any(
                keyword.lower() in body
                for keyword in document.keywords
            ):
                matched.append(document)

        return matched