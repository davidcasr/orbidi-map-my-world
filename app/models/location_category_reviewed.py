from app.core.db import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer


class LocationCategoryReviewed(Base):
    __tablename__ = "location_category_reviewed"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    last_reviewed = Column(DateTime, nullable=False)
