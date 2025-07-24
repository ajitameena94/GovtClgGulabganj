from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.models.user import db

class Timetable(db.Model):
    __tablename__ = "timetables"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    file_url = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)