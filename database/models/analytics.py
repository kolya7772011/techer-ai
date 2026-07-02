from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DailyAnalytics(Base):
    """Daily analytics tracking."""
    __tablename__ = "daily_analytics"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, index=True)
    
    # Metrics
    daily_active_users = Column(Integer, default=0)
    total_ai_requests = Column(Integer, default=0)
    most_popular_subject = Column(String)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<DailyAnalytics(date={self.date})>"
