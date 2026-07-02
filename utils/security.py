import asyncio
import logging
from typing import Optional
from datetime import datetime, timedelta
from functools import wraps

logger = logging.getLogger(__name__)


class RateLimiter:
    """Rate limiter for API requests."""
    
    def __init__(self, requests: int = 10, period: int = 60):
        self.requests = requests
        self.period = period
        self.user_requests: dict[str, list[datetime]] = {}
    
    def is_allowed(self, user_id: str) -> bool:
        """Check if user can make request."""
        now = datetime.utcnow()
        
        if user_id not in self.user_requests:
            self.user_requests[user_id] = []
        
        # Remove old requests
        cutoff = now - timedelta(seconds=self.period)
        self.user_requests[user_id] = [
            req_time for req_time in self.user_requests[user_id]
            if req_time > cutoff
        ]
        
        # Check if allowed
        if len(self.user_requests[user_id]) < self.requests:
            self.user_requests[user_id].append(now)
            return True
        
        return False
    
    def get_remaining(self, user_id: str) -> int:
        """Get remaining requests for user."""
        now = datetime.utcnow()
        
        if user_id not in self.user_requests:
            return self.requests
        
        cutoff = now - timedelta(seconds=self.period)
        recent = [
            req_time for req_time in self.user_requests[user_id]
            if req_time > cutoff
        ]
        
        return max(0, self.requests - len(recent))


def rate_limit(limiter: RateLimiter):
    """Decorator for rate limiting."""
    def decorator(func):
        @wraps(func)
        async def wrapper(update, context):
            user_id = str(update.effective_user.id)
            
            if not limiter.is_allowed(user_id):
                remaining = limiter.get_remaining(user_id)
                await update.message.reply_text(
                    f"⏱️ Siz juda ko'p so'rovlar yuborayapsiz. "
                    f"Iltimos {limiter.period} soniya kutib turing."
                )
                return
            
            return await func(update, context)
        return wrapper
    return decorator


class SecurityValidator:
    """Validate input for security threats."""
    
    @staticmethod
    def validate_input(text: str, max_length: int = 1000) -> Optional[str]:
        """Validate user input."""
        if not text or not isinstance(text, str):
            return None
        
        # Check length
        if len(text) > max_length:
            return None
        
        # Check for prompt injection
        dangerous_patterns = [
            "ignore previous",
            "system prompt",
            "forget your",
            "act as",
        ]
        
        text_lower = text.lower()
        for pattern in dangerous_patterns:
            if pattern in text_lower:
                logger.warning(f"Potential prompt injection detected: {text[:50]}")
                return None
        
        return text.strip()
    
    @staticmethod
    def validate_subject(subject: str) -> bool:
        """Validate subject selection."""
        valid_subjects = [
            "Matematika",
            "Informatika",
            "Fizika",
            "Kimyo",
            "Biologiya",
            "Ingliz tili",
            "Ona tili",
            "Tarix",
            "Geografiya",
        ]
        return subject in valid_subjects
    
    @staticmethod
    def validate_learning_style(style: str) -> bool:
        """Validate learning style."""
        valid_styles = ["Visual", "Auditory", "Reading", "Practice"]
        return style in valid_styles
