# Standard Library
from typing import Optional

# Project
from db.base_class import Base
from pydantic import BaseModel
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


# sqlalchemy
class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


# pydantic


# This class is for shared properties. Its means all
# classes that inherit it will have the same properties.
# Then those classes can add on to it.
## Properties shared by models stored in DB
# This is because we have to set the id for example.
# We cant set the id when creating a note, because its
# set by the DB. But we do want to be able to read it
# after its created
class NoteBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to receive on note creation
class NoteCreate(NoteBase):
    name: str


# Properties to receive on note update
class NoteUpdate(NoteBase):
    pass
