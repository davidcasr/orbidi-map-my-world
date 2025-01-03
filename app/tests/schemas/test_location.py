import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.location import Location
from app.core.db import Base

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


def test_create_location(test_db):
    new_location = Location(
        latitude=40.7128,
        longitude=-74.0060,
        name="Test Location",
        formatted_address="123 Test St, Test City, TC 12345",
        formatted_phone_number="123-456-7890",
        rating=4.5,
        website="http://testlocation.com",
        serves_brunch=True,
        serves_dinner=False,
        serves_lunch=True,
    )
    test_db.add(new_location)
    test_db.commit()
    test_db.refresh(new_location)

    assert new_location.id is not None
    assert new_location.latitude == 40.7128
    assert new_location.longitude == -74.0060
    assert new_location.name == "Test Location"
    assert new_location.formatted_address == "123 Test St, Test City, TC 12345"
    assert new_location.formatted_phone_number == "123-456-7890"
    assert new_location.rating == 4.5
    assert new_location.website == "http://testlocation.com"
    assert new_location.serves_brunch is True
    assert new_location.serves_dinner is False
    assert new_location.serves_lunch is True
