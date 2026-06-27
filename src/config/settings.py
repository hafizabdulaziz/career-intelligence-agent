from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    """
    Production-grade configuration management using Pydantic Settings.
    Environment variables are automatically mapped.
    """
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    APP_NAME: str = "AI Multi-Agent Career Assistant"
    VERSION: str = "1.0.0"
    
    # API Configuration
    GEMINI_API_KEY: Optional[str] = None
    LLM_MODEL: str = "gemini-2.0-flash"
    
    # LLM Parameters
    TEMPERATURE: float = 0.7
    MAX_TOKENS: Optional[int] = None
    
    # Orchestration & Retry Config
    RETRY_COUNT: int = 3
    RETRY_DELAY_SECONDS: int = 15  # Base delay
    TIMEOUT_SECONDS: int = 60
    
    # Logging
    LOG_LEVEL: str = "INFO"

# Instantiate settings (will raise error if GEMINI_API_KEY is missing)
settings = Settings()
