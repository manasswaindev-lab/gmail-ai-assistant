from pathlib import Path
from pydantic import BaseModel, Field


class KnowledgeDocument(BaseModel):
    name: str
    description: str
    keywords: list[str]
    file_name: str
    url: str
    mime_type: str = "application/pdf"

    @property
    def path(self) -> Path:
        return Path(__file__).parent / "resources" / self.file_name


class KnowledgeResult(BaseModel):
    documents: list[KnowledgeDocument] = Field(default_factory=list)

    attachments: list[str] = Field(default_factory=list)

    urls: list[str] = Field(default_factory=list)

    context: str = ""