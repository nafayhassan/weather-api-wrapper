import sys, os
from unittest.mock import AsyncMock, patch
import pytest
from fastapi.testclient import TestClient

# Make sure imports work
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)


# -------- HEALTH CHECK ----------#
def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}


# ----- WEATHER BY CITY ------- #
def test_weather_by_city():
    mock_weather = {
        "temperature": 30.0,
        "description": "Clear sky"
    }
    with patch("services.fetch_weather", new_callable=AsyncMock, return_value=mock_weather):
        response = client.get("/weather/lagos")
        assert response.status_code == 200
        data = response.json()
        assert "temperature" in data
        assert "description" in data
        assert "city" in data
        assert data["city"].lower() == "lagos"


# ------ WEATHER BY COORDINATES --------- #
def test_weather_coordinates():
    mock_weather = {
        "temperature": 28.5,
        "description": "Clear sky"
    }
    with patch("services.fetch_weather_by_coordinates", new_callable=AsyncMock, return_value=mock_weather):
        response = client.get("/weather/coordinates?lat=6.5244&lon=3.3792")
        assert response.status_code == 200
        data = response.json()
        assert "temperature" in data
        assert "description" in data
        assert "city" in data
        assert "(6.5244,3.3792)" in data["city"]


# ------ FORECAST -------------- #
def test_forecast_city():
    mock_forecast = {
        "daily": {
            "temperature_2m_max": [32, 31, 29],
            "temperature_2m_min": [24, 23, 22]
        }
    }
    with patch("services.fetch_forecast", new_callable=AsyncMock, return_value=mock_forecast):
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
    # Insert fake record first
    mock_weather = {
        "temperature": 29.0,
        "description": "Sunny"
    }
    with patch("services.fetch_weather", new_callable=AsyncMock, return_value=mock_weather):
        insert_response = client.get("/weather/Accra")
        assert insert_response.status_code == 200
        data = insert_response.json()
        assert "id" in data
        record_id = int(data["id"])   # ✅ ensure integer

    # Now delete it
    delete_response = client.delete(f"/history/{record_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": f"Record {record_id} Deleted successfully"}


if __name__ == "__main__":
    pytest.main()

