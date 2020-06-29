from fastapi import APIRouter
from typing import List

# import drivers.models
from drivers.models import *

import databases

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./sqlite.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)


router = APIRouter()


@router.get("/", response_model=List[DriverBase], tags=["drivers"])
async def read_drivers():
    # return [{"username": "Foo"}, {"username": "Bar"}]
    drivers = Driver.__table__.select()
    return await database.fetch_all(drivers)


@router.get("/{driver_id}", response_model=DriverBase, tags=["drivers"])
async def read_driver(driver_id: int):
    # return {"driver": driver_id}
    return await database.fetch(Driver)
