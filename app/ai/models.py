from typing import List
from pydantic import BaseModel, Field

class EmailAnalysis(BaseModel):
    summary: str = Field(description="Short summary")
    priority: str = Field(description="High, Medium or Low")
    category: str = Field(description="Email category")
    sentiment: str = Field(description="Positive, Neutral or Negative")
    deadline: str | None = None
    action_items: List[str] = Field(default_factory=list)
    people: List[str] = Field(default_factory=list)
    companies: List[str] = Field(default_factory=list)
    reply_required: bool = False
    suggested_reply: str = ""

class ReplyRequest(BaseModel):
    tone: str = "professional"

class ReplyDocument(BaseModel):
    name: str
    description: str
    url: str
    attachment: str

class ReplyResponse(BaseModel):
    reply: str
    documents: List[ReplyDocument] = Field(default_factory=list)
    attachments: List[str] = Field(default_factory=list)
    urls: List[str] = Field(default_factory=list)
