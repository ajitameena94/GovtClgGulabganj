from pydantic import BaseModel
from datetime import datetime

class NotificationBase(BaseModel):
    title: str
    content: str

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class GalleryItemBase(BaseModel):
    title: str
    category: str

class GalleryItemCreate(GalleryItemBase):
    pass

class GalleryItem(GalleryItemBase):
    id: int
    image_url: str
    uploaded_at: datetime

    class Config:
        orm_mode = True