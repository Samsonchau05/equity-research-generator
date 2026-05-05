"""Configuration management for Equity Research Generator."""

import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment variables."""
    
    # API Keys
    sec_api_key: str = os.getenv("SEC_API_KEY", "demo_key")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    finnhub_api_key: str = os.getenv("FINNHUB_API_KEY", "")
    news_api_key: str = os.getenv("NEWS_API_KEY", "")
    
    # Database
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///research.db")
    
    # Paths
    report_output_dir: str = os.getenv("REPORT_OUTPUT_DIR", "./reports")
    cache_path: str = os.getenv("CACHE_DIR", "./cache")
    
    # LLM Configuration
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4-turbo")
    llm_temperature: float = float(os.getenv("LLM_TEMPERATURE", "0.7"))
    llm_max_tokens: int = int(os.getenv("LLM_MAX_TOKENS", "2000"))
    
    # Cache Settings
    cache_expiry_hours: int = int(os.getenv("CACHE_EXPIRY_HOURS", "24"))
    
    # Report Settings
    include_charts: bool = os.getenv("INCLUDE_CHARTS", "true").lower() == "true"
    include_sources: bool = os.getenv("INCLUDE_SOURCES", "true").lower() == "true"
    
    # Review Workflow
    enable_review_workflow: bool = os.getenv("ENABLE_REVIEW", "true").lower() == "true"
    default_reviewer: Optional[str] = os.getenv("DEFAULT_REVIEWER", None)
    
    # Data Refresh
    refresh_data_on_generate: bool = os.getenv("REFRESH_DATA_ON_GENERATE", "true").lower() == "true"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()

# Ensure output directories exist
os.makedirs(settings.report_output_dir, exist_ok=True)
os.makedirs(settings.cache_path, exist_ok=True)
