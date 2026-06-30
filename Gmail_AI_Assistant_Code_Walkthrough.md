# Gmail AI Assistant - Code Walkthrough

## Source Files

### `gmail-ai-assistant/test_config.py`
- Purpose: Explain this module in project architecture.
- Key imports: from app.core.config import settings
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/__init__.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/main.py`
- Purpose: Explain this module in project architecture.
- Key imports: import os, from fastapi import FastAPI, from starlette.middleware.sessions import SessionMiddleware, from app.api.router import api_router, from app.core.config import settings
- Functions: def root
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/dependencies.py`
- Purpose: Explain this module in project architecture.
- Key imports: from app.database.session import SessionLocal
- Functions: def get_db
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/database/session.py`
- Purpose: Explain this module in project architecture.
- Key imports: from sqlalchemy import create_engine, from sqlalchemy.orm import sessionmaker, from app.core.config import settings
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/database/init__db.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/database/base.py`
- Purpose: Explain this module in project architecture.
- Key imports: from sqlalchemy.orm import DeclarativeBase
- Classes: class Base
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/core/logging.py`
- Purpose: Explain this module in project architecture.
- Key imports: import sys, from loguru import logger
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/core/config.py`
- Purpose: Explain this module in project architecture.
- Key imports: from functools import lru_cache, from pydantic import computed_field, from pydantic_settings import BaseSettings, SettingsConfigDict
- Classes: class Settings
- Functions: def DATABASE_URL, def get_settings
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/core/security.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/core/constants.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/core/__init__.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/ai/service.py`
- Purpose: Explain this module in project architecture.
- Key imports: import json, from app.ai.client import OpenAIClient, from app.ai.models import EmailAnalysis, ReplyResponse, from app.ai.prompt_builder import PromptBuilder, from app.core.config import settings
- Classes: class AIService:
- Functions: def __init__, def analyze_email, def generate_reply
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/ai/models.py`
- Purpose: Explain this module in project architecture.
- Key imports: from typing import List, from pydantic import BaseModel, Field
- Classes: class EmailAnalysis, class ReplyRequest, class ReplyResponse
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/ai/prompt_builder.py`
- Purpose: Explain this module in project architecture.
- Key imports: from app.ai.prompts import (
- Classes: class PromptBuilder:
- Functions: def build_analysis_prompt, def build_reply_prompt
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/ai/client.py`
- Purpose: Explain this module in project architecture.
- Key imports: from openai import OpenAI, from app.core.config import settings
- Classes: class OpenAIClient:
- Functions: def __init__, def get_client
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/ai/__init__.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/ai/prompts.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/ai/reply.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/api/__init__.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/api/router.py`
- Purpose: Explain this module in project architecture.
- Key imports: from fastapi import APIRouter, from app.api.routes.auth import router as auth_router, from app.api.routes.gmail import router as gmail_router, from app.api.routes.health import router as health_router, from app.api.routes.ai import router as ai_router
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/gmail/auth.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/gmail/service.py`
- Purpose: Explain this module in project architecture.
- Key imports: from google.oauth2.credentials import Credentials, from app.gmail.client import GmailClient, from app.gmail.parser import GmailParser
- Classes: class GmailService:
- Functions: def __init__, def get_latest_emails, def get_email, def search_emails, def get_labels
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/gmail/token_store.py`
- Purpose: Explain this module in project architecture.
- Key imports: from google.oauth2.credentials import Credentials
- Classes: class TokenStore:
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/gmail/client.py`
- Purpose: Explain this module in project architecture.
- Key imports: from googleapiclient.discovery import build, from google.oauth2.credentials import Credentials
- Classes: class GmailClient:
- Functions: def __init__, def list_messages, def get_message, def list_labels, def search_messages
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/gmail/__init__.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/gmail/parser.py`
- Purpose: Explain this module in project architecture.
- Key imports: import base64, from typing import Any
- Classes: class GmailParser:
- Functions: def parse_message, def get_header, def extract_body, def extract_parts, def decode_base64
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/gmail/oauth.py`
- Purpose: Explain this module in project architecture.
- Key imports: from google_auth_oauthlib.flow import Flow
- Functions: def create_flow
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/api/routes/auth.py`
- Purpose: Explain this module in project architecture.
- Key imports: from fastapi import APIRouter, Request, from fastapi.responses import RedirectResponse, from app.gmail.oauth import create_flow, from app.gmail.token_store import TokenStore
- Functions: def login, def auth_callback
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/api/routes/health.py`
- Purpose: Explain this module in project architecture.
- Key imports: from fastapi import APIRouter
- Functions: def health
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/api/routes/ai.py`
- Purpose: Explain this module in project architecture.
- Key imports: from fastapi import APIRouter, HTTPException, from app.ai.models import ReplyRequest, from app.ai.service import AIService, from app.gmail.service import GmailService, from app.gmail.token_store import TokenStore
- Functions: def get_gmail_service, def analyze_email, def generate_reply
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/api/routes/__init__.py`
- Purpose: Explain this module in project architecture.
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

### `gmail-ai-assistant/app/api/routes/gmail.py`
- Purpose: Explain this module in project architecture.
- Key imports: from fastapi import APIRouter, HTTPException, Query, from app.gmail.service import GmailService, from app.gmail.token_store import TokenStore
- Functions: def get_service, def list_messages, def get_message, def search_messages, def labels
- Responsibilities:
  - What this file owns.
  - How other modules call it.
  - Expected inputs and outputs.

