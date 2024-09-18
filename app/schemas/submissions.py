from pydantic import BaseModel
from datetime import datetime

class SubmissionCreate(BaseModel):
    image: str
    latitude: float
    longitude: float

class SubmissionResponse(BaseModel):
    id: int
    object_class: str
    latitude: float
    longitude: float
    created_at: datetime

    class Config:
        orm_mode = True