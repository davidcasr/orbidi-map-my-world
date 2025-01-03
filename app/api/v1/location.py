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
    """
    Create a new location entry in the database.

    Args:
        location (LocationCreate): The location data to be created.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db).

    Returns:
        LocationModel: The newly created location entry.
    """
    new_location = LocationModel(
        latitude=location.latitude,
        longitude=location.longitude,
        name=location.name,
        formatted_address=location.formatted_address,
        formatted_phone_number=location.formatted_phone_number,
        rating=location.rating,
        website=location.website,
        serves_brunch=location.serves_brunch,
        serves_dinner=location.serves_dinner,
        serves_lunch=location.serves_lunch,
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
    """
    Retrieve all locations from the database.

    Args:
        db (Session): Database session dependency.

    Returns:
        List[LocationModel]: A list of all location records.
    """
    locations = db.query(LocationModel).all()
    return locations


@router.get(
    "/{location_id}",
    response_model=Location,
    summary="Get a location",
    description="Get a location by its ID.",
)
def get_location(location_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a location by its ID from the database.

    Args:
        location_id (int): The ID of the location to retrieve.
        db (Session, optional): The database session dependency. Defaults to Depends(get_db).

    Returns:
        LocationModel: The location object if found.

    Raises:
        HTTPException: If the location is not found, raises a 404 HTTP exception with the message "Location not found".
    """
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
    """
    Delete a location from the database.
    Args:
        location_id (int): The ID of the location to be deleted.
        db (Session, optional): The database session. Defaults to Depends(get_db).
    Raises:
        HTTPException: If the location with the given ID is not found.
    Returns:
        LocationModel: The deleted location object.
    """
    location = db.query(LocationModel).filter(LocationModel.id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    db.delete(location)
    db.commit()
    return location
