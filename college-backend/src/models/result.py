from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    file_url = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
