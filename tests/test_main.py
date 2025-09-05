import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# -------- HEALTH CHECK ----------#
def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}


# ----- WEATHER BY CITY ------- #
def test_weather_by_city():
    response = client.get("/weather/lagos")
    assert response.status_code == 200
    data = response.json()
    assert "temperature" in data
    assert "description" in data
    assert "city" in data
    assert data["city"].lower() == "lagos"


# ------ WEATHER BY CO ORDINATES --------- #
def test_weather_coordinates():
    response = client.get("/weather/coordinates?lat=6.5244&lon=3.3792")
    assert response.status_code == 200
    data = response.json()
    assert "temperature" in data
    assert "description" in data
    assert "city" in data
    assert "(6.5244,3.3792)" in data["city"]


# ------ FORECAST -------------- #
def test_forecast_city():

