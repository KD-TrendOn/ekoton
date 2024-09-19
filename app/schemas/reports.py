from pydantic import BaseModel
from typing import Dict

class ParkReport(BaseModel):
    statistics: Dict[str, int]