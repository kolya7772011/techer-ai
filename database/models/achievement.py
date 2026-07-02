from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Achievement(Base):
    """Achievement definitions."""
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    icon = Column(String)  # emoji
    xp_reward = Column(Integer, default=0)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<Achievement(code={self.code}, name={self.name})>"


class UserAchievement(Base):
    """User achievements tracking."""
    __tablename__ = "user_achievements"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, ForeignKey("users.telegram_id"), nullable=False, index=True)
    achievement_code = Column(String, ForeignKey("achievements.code"), nullable=False)
    unlocked_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<UserAchievement(telegram_id={self.telegram_id}, code={self.achievement_code})>"
