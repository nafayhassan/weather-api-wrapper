from datetime import datetime
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import schemas
import services
from database import engine, SessionLocal
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Weather API Wrapper")


# Dependency: DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/weather/{city}", response_model=schemas.WeatherResponse)
async def get_weather(city: str, db: Session = Depends(get_db)):
    weather = await services.fetch_weather(city)
    if not weather:
        return {
            "city": city,
            "temperature": 0,
            "description": "Not found",
            "timestamp": datetime.utcnow()
        }

    db_weather = models.WeatherHistory(
        city=city,
        temperature=weather["temperature"],
        description=weather["description"],
    )
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)

    return db_weather


@app.get("/history", response_model=List[schemas.WeatherResponse])
def get_history(db: Session = Depends(get_db)):
    return db.query(models.WeatherHistory).all()


# GET WEATHER BY C0 ORDINATES
app.get("/weather/coordinates")


async def get_weather_coordinates(lat: float, lon: float, db: Session = Depends(get_db)):
    weather = await services.fetch_weather_by_coordinates(lat, lon)
    if not weather:
        return {"lat": lat, "lon": lon, "description": "not found"}

    db_weather = models.WeatherHistory(
        city=f"({lat},{lon})",
        temperature=weather["temperature"],
        description=weather["description"]
    )
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)

    return db_weather

