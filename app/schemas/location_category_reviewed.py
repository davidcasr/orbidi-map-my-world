from datetime import datetime
from pydantic import BaseModel


class LocationCategoryReviewedBase(BaseModel):
    location_id: int
    category_id: int


class LocationCategoryReviewedCreate(LocationCategoryReviewedBase):
    pass


class LocationCategoryReviewed(LocationCategoryReviewedBase):
    id: int
    last_reviewed: datetime

    class Config:
        orm_mode = True
