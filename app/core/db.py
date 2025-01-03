from app.core.config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Dependency generator function that provides a database session.

    This function is designed to be used with FastAPI's dependency injection system.
    It yields a database session and ensures that the session is properly closed
    after the request is completed.

    Yields:
        SessionLocal: A SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
