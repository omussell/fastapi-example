# Standard Library
from typing import Optional

# 3rd-party
import databases
import orm
import sqlalchemy
from pydantic import BaseModel

# Project
from db.base import database
from db.base import metadata
from notebooks.models import Notebook

# sqlalchemy


class Note(orm.Model):
    __tablename__ = "notes"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True, index=True)
    notebook = orm.ForeignKey(Notebook)
    text = orm.String(max_length=100)
    completed = orm.Boolean(default=False)


# pydantic


class NoteBase(BaseModel):
    notebook: str
    text: Optional[str]
    completed: Optional[bool]

    class Config:
        orm_mode = True


class NoteCreate(NoteBase):
    text: str
    completed: Optional[bool] = False


class NoteRead(NoteBase):
    id: int


class NoteUpdate(NoteBase):
    id: int


class NoteDelete(NoteBase):
    id: int
