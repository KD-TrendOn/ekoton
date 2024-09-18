# app/schemas/reports.py

from pydantic import BaseModel
from datetime import datetime

class ReportResponse(BaseModel):
    id: int
    object_class: str
    latitude: float
    longitude: float
    created_at: datetime

    class Config:
        orm_mode = True
