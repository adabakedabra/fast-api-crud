import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_read_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []

def test_create_item():
    data = {"id": 1, "name": "Test Item", "price": 10.99}
    response = client.post("/items", json=data)
    assert response.status_code == 200
    assert response.json() == data

