import logging
import json
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from database.models import User, DailyAnalytics
from config import settings

logger = logging.getLogger(__name__)


class JSONFormatter(logging.Formatter):
    """Custom JSON formatter for logging."""
    
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_data, ensure_ascii=False)


def setup_logging() -> None:
    """Setup logging configuration."""
    log_dir = "logs"
    import os
    os.makedirs(log_dir, exist_ok=True)
    
    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, settings.LOG_LEVEL))
    
    # File handler
    file_handler = logging.FileHandler(f"{log_dir}/app.log")
    file_handler.setFormatter(JSONFormatter())
    root_logger.addHandler(file_handler)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    root_logger.addHandler(console_handler)
    
    # Error log file
    error_handler = logging.FileHandler(f"{log_dir}/error.log")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(JSONFormatter())
    root_logger.addHandler(error_handler)


def get_logger(name: str) -> logging.Logger:
    """Get logger instance."""
    return logging.getLogger(name)
