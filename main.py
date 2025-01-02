from app.core.db import Base, engine
from app.api.v1 import category, location_category_reviewed, location
from app.core.error_handler import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler,
)
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

# The following lines of code are used for initial development only
# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Map My World API",
    description="API for exploring locations and categories, managing reviews and recommendations.",
    version="1.0.0",
    contact={
        "name": "Map My World Support",
        "email": "me@davidcasr.com",
        "url": "https://davidcasr.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(location.router, prefix="/locations", tags=["Locations"])
app.include_router(category.router, prefix="/categories", tags=["Categories"])
app.include_router(
    location_category_reviewed.router, prefix="/reviews", tags=["Reviews"]
)


@app.get(
    "/",
    summary="Check system status",
    description="Endpoint to check if the API is working correctly.",
    tags=["Health | Review Home"],
    responses={200: {"description": "The system is operational"}},
)
def get_home():
    return {"message": "Welcome to the Map My World API!"}
