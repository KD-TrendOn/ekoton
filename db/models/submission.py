from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from .base import Base

class Submission(Base):
    __tablename__ = "submissions"

    image = Column(String, nullable=False)  # base64 строка изображения
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    object_class = Column(String, nullable=False)  # 'flora' или 'fauna'
    status = Column(String, default="pending")  # 'pending', 'approved', 'rejected'
    created_at = Column(DateTime(timezone=True), server_default=func.now())

