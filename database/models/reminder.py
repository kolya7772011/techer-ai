from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Reminder(Base):
    """Daily reminders settings."""
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, ForeignKey("users.telegram_id"), nullable=False, index=True, unique=True)
    
    is_enabled = Column(Boolean, default=True)
    reminder_time = Column(String, nullable=False, default="09:00")  # HH:MM
    
    last_sent_at = Column(DateTime)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<Reminder(telegram_id={self.telegram_id}, enabled={self.is_enabled})>"
