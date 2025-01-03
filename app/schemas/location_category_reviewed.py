from datetime import datetime
from pydantic import BaseModel, ConfigDict


class LocationCategoryReviewedBase(BaseModel):
    location_id: int
    category_id: int


class LocationCategoryReviewedCreate(LocationCategoryReviewedBase):
    pass


class LocationCategoryReviewed(LocationCategoryReviewedBase):
    id: int
    last_reviewed: datetime

    model_config = ConfigDict(from_attributes=True)


class LocationCategoryUpdate(BaseModel):
    location_id: int
    category_id: int
