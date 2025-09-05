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