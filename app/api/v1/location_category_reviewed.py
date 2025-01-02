from app.schemas.location_category_reviewed import (
    LocationCategoryReviewed,
    LocationCategoryReviewedCreate,
)
from app.models.location_category_reviewed import (
    LocationCategoryReviewed as ReviewModel,
)
from app.core.db import get_db
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post(
    "/",
    response_model=LocationCategoryReviewed,
    summary="Create a review",
    description="Create a new review.",
)
def create_review(
    review: LocationCategoryReviewedCreate, db: Session = Depends(get_db)
):
    new_review = ReviewModel(
        location_id=review.location_id,
        category_id=review.category_id,
        last_reviewed=datetime.utcnow(),
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review


@router.get(
    "/",
    response_model=list[LocationCategoryReviewed],
    summary="Get all reviews",
    description="Get all reviews available in the system.",
)
def get_reviews(db: Session = Depends(get_db)):
    reviews = db.query(ReviewModel).all()
    return reviews


@router.get(
    "/pending",
    response_model=list[LocationCategoryReviewed],
    summary="Get all pending reviews",
    description="Get all reviews that have not been reviewed in the last 30 days.",
)
def get_pending_reviews(db: Session = Depends(get_db)):
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    pending_reviews = (
        db.query(ReviewModel).filter(ReviewModel.last_reviewed < thirty_days_ago).all()
    )
    return pending_reviews


@router.delete(
    "/{review_id}",
    response_model=LocationCategoryReviewed,
    summary="Delete a review",
    description="Delete a review by its ID.",
)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    db.delete(review)
    db.commit()
    return review
