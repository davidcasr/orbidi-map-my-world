import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from app.core.db import Base, get_db
from app.models.location_category_reviewed import (
    LocationCategoryReviewed as ReviewModel,
)

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


def test_create_review(test_db):
    response = client.post("/v1/reviews/", json={"location_id": 1, "category_id": 1})
    assert response.status_code == 200
    assert response.json()["location_id"] == 1
    assert response.json()["category_id"] == 1


def test_get_reviews(test_db):
    response = client.get("/v1/reviews/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_review_recommendations(test_db):
    client.post("/v1/reviews/", json={"location_id": 1, "category_id": 1})
    response = client.put(
        "/v1/reviews/recommendations", json={"location_id": 1, "category_id": 1}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Review date updated successfully"
    assert response.json()["review"]["location_id"] == 1
    assert response.json()["review"]["category_id"] == 1


def test_update_review_recommendations_not_found(test_db):
    response = client.put(
        "/v1/reviews/recommendations", json={"location_id": 999, "category_id": 999}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Review not found"
