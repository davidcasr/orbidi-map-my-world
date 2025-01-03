from app.schemas.location_category_reviewed import (
    LocationCategoryReviewed,
    LocationCategoryReviewedCreate,
    LocationCategoryUpdate,
)
from app.models.location_category_reviewed import (
    LocationCategoryReviewed as ReviewModel,
)
from app.core.db import get_db
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
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
    """
    Create a new review for a location category.

    Args:
        review (LocationCategoryReviewedCreate): The review data to be created.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        ReviewModel: The newly created review object.
    """
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
    summary="Get all the last reviews",
    description="Get all reviews that have not been reviewed in the last 30 days.",
)
def get_reviews(db: Session = Depends(get_db)):
    """
    Retrieve reviews that were last reviewed more than 30 days ago.

    Args:
        db (Session): Database session dependency.

    Returns:
        List[ReviewModel]: A list of reviews that were last reviewed more than 30 days ago.
    """
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    recommendations = (
        db.query(ReviewModel).filter(ReviewModel.last_reviewed < thirty_days_ago).all()
    )
    return recommendations


@router.put(
    "/recommendations",
    summary="Update review date",
    description="Update the last_reviewed date for a given location_id and category_id.",
)
def update_review_recommendations(
    review_update: LocationCategoryUpdate, db: Session = Depends(get_db)
):
    """
    Update the review recommendations for a specific location and category.
    This function updates the last reviewed date of a review based on the provided
    location and category IDs. If the review does not exist, it raises a 404 HTTP
    exception.
    Args:
        review_update (LocationCategoryUpdate): An object containing the location_id
            and category_id to identify the review to be updated.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db).
    Raises:
        HTTPException: If the review is not found, a 404 status code is returned.
    Returns:
        dict: A dictionary containing a success message and the updated review object.
    """
    review = (
        db.query(ReviewModel)
        .filter(
            ReviewModel.location_id == review_update.location_id,
            ReviewModel.category_id == review_update.category_id,
        )
        .first()
    )

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    review.last_reviewed = datetime.utcnow()
    db.commit()
    db.refresh(review)
    return {"message": "Review date updated successfully", "review": review}
