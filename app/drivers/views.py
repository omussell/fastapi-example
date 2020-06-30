# Standard Library
from typing import List

# Project
import databases
# import drivers.models
from app.drivers.models import *
from fastapi import APIRouter

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./sqlite.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)


router = APIRouter()


@router.get("/", response_model=List[DriverBase], tags=["drivers"])
async def read_drivers(url: str = None):
    """
    Summary line

    Usage:

    ```python
    x = "gongiveittoya"
    ```

    **Parameters:**

    * **url** - *optional* Optionally give the URL.
    """
    # return [{"username": "Foo"}, {"username": "Bar"}]
    drivers = Driver.__table__.select()
    return await database.fetch_all(drivers)


@router.get("/{driver_id}", response_model=DriverBase, tags=["drivers"])
async def read_driver(driver_id: int):
    # return {"driver": driver_id}
    return await database.fetch(Driver)
