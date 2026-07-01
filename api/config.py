"""Rockbusters API configuration — reads settings from environment variables."""

import os
from dataclasses import dataclass, field

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    """Application configuration sourced from environment variables.

    All fields fall back to sensible defaults so the app runs locally
    without any .env file.
    """

    sqlite_path: str = field(
        default_factory=lambda: os.getenv("SQLITE_PATH", "rockbusters.db")
    )
    bank_path: str = field(
        default_factory=lambda: os.getenv(
            "ROCKBUSTERS_BANK_PATH", "data/rockbusters.yaml"
        )
    )
    timezone: str = field(
        default_factory=lambda: os.getenv("APP_TIMEZONE", "Europe/London")
    )
    allowed_origins: str = field(
        default_factory=lambda: os.getenv("ALLOWED_ORIGINS", "*")
    )
    api_secret: str = field(
        default_factory=lambda: os.getenv("API_SECRET", "")
    )
