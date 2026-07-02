import json
from pathlib import Path

from app.knowledge.models import KnowledgeDocument


class KnowledgeRepository:

    def __init__(self):

        self.file = (
            Path(__file__).parent
            / "knowledge.json"
        )

    def get_documents(self):

        with open(self.file, encoding="utf-8") as f:

            data = json.load(f)

        return [
            KnowledgeDocument.model_validate(d)
            for d in data
        ]