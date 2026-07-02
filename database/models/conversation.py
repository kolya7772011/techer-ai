from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ConversationHistory(Base):
    """Store conversation history for context."""
    __tablename__ = "conversation_history"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, ForeignKey("users.telegram_id"), nullable=False, index=True)
    subject = Column(String, nullable=False)
    topic = Column(String, nullable=False)
    
    role = Column(String, nullable=False)  # 'user' or 'assistant'
    message = Column(Text, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    
    def __repr__(self) -> str:
        return f"<ConversationHistory(telegram_id={self.telegram_id}, subject={self.subject})>"
