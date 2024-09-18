
from sqlalchemy import Column, String, Text, DateTime, Boolean, Integer
from sqlalchemy.sql import func
from .base import Base

class Task(Base):
    __tablename__ = "tasks"

    title = Column(String, nullable=False)
    image = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)