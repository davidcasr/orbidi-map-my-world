from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """
    Handles HTTP exceptions and returns a JSON response with the error details.

    Args:
        request (Request): The incoming HTTP request.
        exc (StarletteHTTPException): The HTTP exception that was raised.

    Returns:
        JSONResponse: A JSON response containing the status code and error details.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Asynchronous handler for request validation errors.

    This function handles exceptions of type `RequestValidationError` that occur
    during request validation. It returns a JSON response with a status code of 422
    (Unprocessable Entity) and a detailed error message.

    Args:
        request (Request): The incoming HTTP request.
        exc (RequestValidationError): The validation error exception.

    Returns:
        JSONResponse: A JSON response containing the validation error details.
    """
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )


async def generic_exception_handler(request: Request, exc: Exception):
    """
    Handles generic exceptions and returns a JSON response with a 500 status code.

    Args:
        request (Request): The incoming request that caused the exception.
        exc (Exception): The exception that was raised.

    Returns:
        JSONResponse: A JSON response with a 500 status code and a message indicating an internal server error.
    """
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )
