# app/schemas/tasks.py

from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str = None
    created_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
