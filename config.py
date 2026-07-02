import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # Telegram
    TELEGRAM_BOT_TOKEN: str
    
    # Gemini
    GEMINI_API_KEY: str
    
    # Database
    DATABASE_URL: str = "sqlite:///./teacher_bot.db"
    
    # Railway
    RAILWAY_PORT: int = 8000
    WEBHOOK_URL: Optional[str] = None
    
    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # Pagination
    LEADERBOARD_PAGE_SIZE: int = 10
    
    # XP Settings
    XP_PER_ANSWER: int = 10
    XP_PER_LEVEL: int = 100
    
    # Rate limiting
    RATE_LIMIT_REQUESTS: int = 10
    RATE_LIMIT_PERIOD: int = 60  # seconds
    
    # AI
    MAX_CONTEXT_MESSAGES: int = 20
    AI_TIMEOUT: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
