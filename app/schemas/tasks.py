# app/schemas/tasks.py

from pydantic import BaseModel
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

    class Config:
        orm_mode = True
