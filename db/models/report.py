from sqlalchemy import Column, String, Text, DateTime, Integer
from sqlalchemy.sql import func
from .base import Base

class Report(Base):
    __tablename__ = "reports"

    generated_at = Column(DateTime(timezone=True), server_default=func.now())
    content = Column(Text, nullable=False)  # JSON или текст отчета
