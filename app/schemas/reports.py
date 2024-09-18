# app/schemas/reports.py

from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ReportResponse(BaseModel):
    id: int
    object_class: str
    latitude: float
    longitude: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)