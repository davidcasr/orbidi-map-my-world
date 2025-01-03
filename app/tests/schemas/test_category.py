import pytest
from pydantic import ValidationError
from app.schemas.category import CategoryBase, CategoryCreate, Category


def test_category_base():
    category = CategoryBase(name="Test Category")
    assert category.name == "Test Category"


def test_category_base_invalid():
    with pytest.raises(ValidationError):
        CategoryBase(name=123)


def test_category_create():
    category = CategoryCreate(name="Test Category Create")
    assert category.name == "Test Category Create"


def test_category():
    category = Category(id=1, name="Test Category")
    assert category.id == 1
    assert category.name == "Test Category"


def test_category_invalid():
    with pytest.raises(ValidationError):
        Category(id="one", name="Test Category")
