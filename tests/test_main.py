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
    response = client.get("/forecast/London?days=3")
    assert response.status_code == 200
    data = response.json()
    assert "city" in data
    assert data["city"].lower() == "london"
    assert "daily" in data
    assert "temperature_2m_max" in data["daily"]
    assert len(data["daily"]["temperature_2m_max"]) == 3


# -------- HISTORY ----------- #
def test_get_history():
    response = client.get("/history")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert "city" in data[0]
        assert "temperature" in data[0]


# -------- CITIES ----------- #
def test_get_cities():
    response = client.get("/cities")
    assert response.status_code == 200
    data = response.json()
    assert "cities" in data
    assert isinstance(data["cities"], list)


# -------- DELETE HISTORY RECORD --------- #
def test_delete_records():
    # insert a weather record
    insert_response = client.get("/weather/Accra")
    assert insert_response.status_code == 200
    record_id = insert_response.json()["id"]

    # delete inserted record
    delete_response = client.delete(f"/history/{record_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": f"Record {record_id} Deleted successfully"}

