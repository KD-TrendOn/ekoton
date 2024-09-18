from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)