from app.core.db import get_db
from app.schemas.location import Location, LocationCreate
from app.models.location import Location as LocationModel
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post(
    "/",
    response_model=Location,
    summary="Create a location",
    description="Create a new location.",
)
def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    new_location = LocationModel(
        latitude=location.latitude, longitude=location.longitude
    )
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location


@router.get(
    "/",
    response_model=list[Location],
    summary="Get all locations",
    description="Get all locations available in the system.",
)
def get_locations(db: Session = Depends(get_db)):
    locations = db.query(LocationModel).all()
    return locations


@router.get(
    "/{location_id}",
    response_model=Location,
    summary="Get a location",
    description="Get a location by its ID.",
)
def get_location(location_id: int, db: Session = Depends(get_db)):
    location = db.query(LocationModel).filter(LocationModel.id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


@router.delete(
    "/{location_id}",
    response_model=Location,
    summary="Delete a location",
    description="Delete a location by its ID.",
)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    location = db.query(LocationModel).filter(LocationModel.id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    db.delete(location)
    db.commit()
    return location
