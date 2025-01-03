import pytest
from datetime import datetime
from pydantic import ValidationError

from app.schemas.location_category_reviewed import (
    LocationCategoryReviewedBase,
    LocationCategoryReviewedCreate,
    LocationCategoryReviewed,
    LocationCategoryUpdate,
)


def test_location_category_reviewed_base():
    data = {"location_id": 1, "category_id": 2}
    model = LocationCategoryReviewedBase(**data)
    assert model.location_id == 1
    assert model.category_id == 2


def test_location_category_reviewed_create():
    data = {"location_id": 1, "category_id": 2}
    model = LocationCategoryReviewedCreate(**data)
    assert model.location_id == 1
    assert model.category_id == 2


def test_location_category_reviewed():
    data = {
        "id": 1,
        "location_id": 1,
        "category_id": 2,
        "last_reviewed": datetime.now(),
    }
    model = LocationCategoryReviewed(**data)
    assert model.id == 1
    assert model.location_id == 1
    assert model.category_id == 2
    assert isinstance(model.last_reviewed, datetime)


def test_location_category_update():
    data = {"location_id": 1, "category_id": 2}
    model = LocationCategoryUpdate(**data)
    assert model.location_id == 1
    assert model.category_id == 2


def test_invalid_location_category_reviewed_base():
    data = {"location_id": "invalid", "category_id": 2}
    with pytest.raises(ValidationError):
        LocationCategoryReviewedBase(**data)


def test_invalid_location_category_reviewed():
    data = {
        "id": 1,
        "location_id": 1,
        "category_id": 2,
        "last_reviewed": "invalid_date",
    }
    with pytest.raises(ValidationError):
        LocationCategoryReviewed(**data)
