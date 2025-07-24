from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.models.user import db

class Notification(db.Model):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)