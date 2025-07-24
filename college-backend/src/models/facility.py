from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.models.user import db

class Facility(db.Model):
    __tablename__ = "facilities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    image_url = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)