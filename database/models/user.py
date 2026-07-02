from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User model for storing user profile data."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True, nullable=False, index=True)
    full_name = Column(String, nullable=False)
    class_level = Column(String, nullable=False)  # 5-sinf, 6-sinf, etc.
    subject = Column(String, nullable=False)  # Matematika, Fizika, etc.
    learning_style = Column(String, nullable=False)  # Visual, Auditory, Reading, Practice
    
    # XP and Level
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    
    # Streaks
    streak_count = Column(Integer, default=0)
    last_active = Column(DateTime, default=datetime.utcnow)
    
    # Reminder settings
    reminder_enabled = Column(Boolean, default=True)
    reminder_time = Column(String, default="09:00")  # HH:MM format
    
    # Account
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<User(telegram_id={self.telegram_id}, full_name={self.full_name})>"
