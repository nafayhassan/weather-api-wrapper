from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class WeatherResponse(BaseModel):
    id: Optional[int] = None
    city: str
    temperature: float
    description: str
    timestamp: datetime

    class Config:
        from_attributes = True
