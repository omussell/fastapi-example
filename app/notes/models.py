# Standard Library
from typing import Optional

# Project
from db.base import database, metadata
from pydantic import BaseModel
import sqlalchemy
import databases
import orm


# sqlalchemy

class Note(orm.Model):
    __tablename__ = "notes"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True, index=True)
    text = orm.String(max_length=100)
    completed = orm.Boolean(default=False)


# pydantic

class NoteBase(BaseModel):
    id: int
    text: str
    completed: bool

    class Config:
        orm_mode = True

class NoteCreate(NoteBase):
    text: str
    completed: Optional[bool] = False

class NoteUpdate(NoteBase):
    text: Optional[str]
    completed: Optional[bool]
