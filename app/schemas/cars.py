from typing import Optional

from pydantic import BaseModel


# This class is for shared properties. Its means all
# classes that inherit it will have the same properties.
# Then those classes can add on to it.
class CarBase(BaseModel):
    description: Optional[str] = None


# Properties to receive on car creation
class CarCreate(CarBase):
    name: str


# Properties to receive on car update
class CarUpdate(CarBase):
    pass


## Properties shared by models stored in DB
# This is because we have to set the id for example.
# We cant set the id when creating a car, because its
# set by the DB. But we do want to be able to read it
# after its created
class Car(CarBase):
    id: int
    name: str
    description: str
    driver_id: int
    trip_id: int

    class Config:
        orm_mode = True
