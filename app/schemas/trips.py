from typing import Optional

from pydantic import BaseModel


# This class is for shared properties. Its means all
# classes that inherit it will have the same properties.
# Then those classes can add on to it.
class TripBase(BaseModel):
    description: Optional[str] = None


# Properties to receive on trip creation
class TripCreate(TripBase):
    name: str


# Properties to receive on trip update
class TripUpdate(TripBase):
    pass


## Properties shared by models stored in DB
# This is because we have to set the id for example.
# We cant set the id when creating a trip, because its
# set by the DB. But we do want to be able to read it
# after its created
class Trip(TripBase):
    id: int
    name: str
    description: str
    car_id: int

    class Config:
        orm_mode = True
