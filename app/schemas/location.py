from pydantic import BaseModel, field_validator, ConfigDict
from typing import Optional


class LocationBase(BaseModel):
    latitude: float
    longitude: float
    name: str
    formatted_address: Optional[str] = None
    formatted_phone_number: Optional[str] = None
    rating: Optional[float] = None
    website: Optional[str] = None
    serves_brunch: Optional[bool] = False
    serves_dinner: Optional[bool] = False
    serves_lunch: Optional[bool] = False


class LocationCreate(LocationBase):
    @field_validator("latitude")
    @classmethod
    def validate_latitude(cls, value):
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        return value

    @field_validator("longitude")
    @classmethod
    def validate_longitude(cls, value):
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        return value

    @field_validator("rating")
    @classmethod
    def validate_rating(cls, value):
        if value is not None and not (0 <= value <= 5):
            raise ValueError("Rating must be between 0 and 5.")
        return value


class Location(LocationBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
