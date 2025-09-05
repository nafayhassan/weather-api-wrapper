from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base


class WeatherHistory(Base):
    __tablename__ = "weather_history"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

