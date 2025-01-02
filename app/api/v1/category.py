from app.schemas.category import Category, CategoryCreate
from app.models.category import Category as CategoryModel
from app.core.db import get_db
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post(
    "/",
    response_model=Category,
    summary="Create a category",
    description="Create a new category.",
)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = (
        db.query(CategoryModel).filter(CategoryModel.name == category.name).first()
    )
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")

    new_category = CategoryModel(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@router.get(
    "/",
    response_model=list[Category],
    summary="Get all categories",
    description="Get all categories available in the system.",
)
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(CategoryModel).all()
    return categories


@router.get(
    "/{category_id}",
    response_model=Category,
    summary="Get a category",
    description="Get a category by its ID.",
)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete(
    "/{category_id}",
    response_model=Category,
    summary="Delete a category",
    description="Delete a category by its ID.",
)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()
    return category
