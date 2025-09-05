import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# -------- HEALTH CHECK ----------#
def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}
