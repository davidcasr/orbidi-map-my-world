import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from app.core.db import Base, get_db
from app.models.location import Location as LocationModel

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_create_location(test_db):
    response = client.post(
        "/v1/locations/",
        json={"name": "New York Park", "latitude": 40.7128, "longitude": -74.0060},
    )
    assert response.status_code == 200
    assert response.json()["latitude"] == 40.7128
    assert response.json()["longitude"] == -74.0060


def test_get_locations(test_db):
    response = client.get("/v1/locations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_location(test_db):
    response = client.post(
        "/v1/locations/",
        json={"name": "New York Park", "latitude": 34.0522, "longitude": -118.2437},
    )
    location_id = response.json()["id"]
    response = client.get(f"/v1/locations/{location_id}")
    assert response.status_code == 200
    assert response.json()["latitude"] == 34.0522
    assert response.json()["longitude"] == -118.2437


def test_get_location_not_found(test_db):
    response = client.get("/v1/locations/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Location not found"


def test_delete_location(test_db):
    response = client.post(
        "/v1/locations/",
        json={"name": "New York Park", "latitude": 51.5074, "longitude": -0.1278},
    )
    location_id = response.json()["id"]
    response = client.delete(f"/v1/locations/{location_id}")
    assert response.status_code == 200
    assert response.json()["latitude"] == 51.5074
    assert response.json()["longitude"] == -0.1278


def test_delete_location_not_found(test_db):
    response = client.delete("/v1/locations/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Location not found"
