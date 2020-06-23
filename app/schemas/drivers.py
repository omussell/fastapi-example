from typing import Optional

from pydantic import BaseModel


# This class is for shared properties. Its means all
# classes that inherit it will have the same properties.
# Then those classes can add on to it.
class DriverBase(BaseModel):
    description: Optional[str] = None


# Properties to receive on driver creation
class DriverCreate(DriverBase):
    name: str


# Properties to receive on driver update
class DriverUpdate(DriverBase):
    pass


## Properties shared by models stored in DB
# This is because we have to set the id for example.
# We cant set the id when creating a driver, because its
# set by the DB. But we do want to be able to read it
# after its created
class Driver(DriverBase):
    id: int
    name: str
    car_id: int

    class Config:
        orm_mode = True
