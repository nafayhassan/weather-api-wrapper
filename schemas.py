from pydantic import BaseModel
from datetime import datetime


class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
    timestamp: datetime

    class Config:
        form_attributes = True
