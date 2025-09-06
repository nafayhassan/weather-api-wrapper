from pydantic import BaseModel
from datetime import datetime


class WeatherResponse(BaseModel):
    id: int
    city: str
    temperature: float
    description: str
    timestamp: datetime

    class Config:
        orm_mode = True
