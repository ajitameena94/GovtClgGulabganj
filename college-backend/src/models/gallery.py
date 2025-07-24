from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.models.user import db

class GalleryItem(db.Model):
    __tablename__ = "gallery_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    image_url = Column(String)
    category = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)