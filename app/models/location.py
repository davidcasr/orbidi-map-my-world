from sqlalchemy import Column, Float, Integer, String, Boolean
from app.core.db import Base


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    formatted_address = Column(String, nullable=True)
    formatted_phone_number = Column(String, nullable=True)
    name = Column(String, nullable=False)
    rating = Column(Float, nullable=True)
    website = Column(String, nullable=True)
    serves_brunch = Column(Boolean, default=False)
    serves_dinner = Column(Boolean, default=False)
    serves_lunch = Column(Boolean, default=False)
