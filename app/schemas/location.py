from pydantic import BaseModel, validator
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
    @validator("latitude")
    def latitude_must_be_valid(cls, value):
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90.")
        return value

    @validator("longitude")
    def longitude_must_be_valid(cls, value):
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180.")
        return value


class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True
