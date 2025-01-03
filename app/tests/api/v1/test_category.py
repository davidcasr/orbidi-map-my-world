import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from app.core.db import Base, get_db
from app.models.category import Category as CategoryModel

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


def test_create_category(test_db):
    response = client.post("/v1/categories/", json={"name": "Test Category"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Category"


def test_create_existing_category(test_db):
    client.post("/v1/categories/", json={"name": "Test Category"})
    response = client.post("/v1/categories/", json={"name": "Test Category"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Category already exists"


def test_get_categories(test_db):
    client.post("/v1/categories/", json={"name": "Category 1"})
    client.post("/v1/categories/", json={"name": "Category 2"})
    response = client.get("/v1/categories/")
    assert response.status_code == 200


def test_get_category(test_db):
    response = client.post("/v1/categories/", json={"name": "Single Category"})
    category_id = response.json()["id"]
    response = client.get(f"/v1/categories/{category_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Single Category"


def test_get_nonexistent_category(test_db):
    response = client.get("/v1/categories/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Category not found"


def test_delete_category(test_db):
    response = client.post("/v1/categories/", json={"name": "Delete Category"})
    category_id = response.json()["id"]
    response = client.delete(f"/v1/categories/{category_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Delete Category"


def test_delete_nonexistent_category(test_db):
    response = client.delete("/v1/categories/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Category not found"
