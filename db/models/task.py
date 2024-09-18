from sqlalchemy import Column, String, Text, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.sql import func
from .base import Base
from sqlalchemy.orm import relationship
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    target_flora = Column(String, nullable=True)  # Названия растений
    target_fauna = Column(String, nullable=True)  # Названия животных
    area_id = Column(Integer, ForeignKey("areas.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    area = relationship("Area")