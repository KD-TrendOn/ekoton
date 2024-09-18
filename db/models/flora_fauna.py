from sqlalchemy import Column, String, Text, Integer
from .base import Base

class FloraFauna(Base):
    __tablename__ = "flora_fauna"

    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String, nullable=False)  # 'flora' или 'fauna'
    habitat = Column(String, nullable=True)
    characteristics = Column(Text, nullable=True)
