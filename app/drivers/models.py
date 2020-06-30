# Standard Library
from typing import Optional

# Project
from app.db.base_class import Base
from pydantic import BaseModel
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


# sqlalchemy
class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


# pydantic


# This class is for shared properties. Its means all
# classes that inherit it will have the same properties.
# Then those classes can add on to it.
## Properties shared by models stored in DB
# This is because we have to set the id for example.
# We cant set the id when creating a driver, because its
# set by the DB. But we do want to be able to read it
# after its created
class DriverBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to receive on driver creation
class DriverCreate(DriverBase):
    name: str


# Properties to receive on driver update
class DriverUpdate(DriverBase):
    pass
