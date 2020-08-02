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

# sqlalchemy


class Notebook(orm.Model):
    __tablename__ = "notebooks"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True, index=True)
    name = orm.String(max_length=100)


# pydantic


class NotebookBase(BaseModel):
    name: Optional[str]

    class Config:
        orm_mode = True


class NotebookCreate(NotebookBase):
    pass


class NotebookRead(NotebookBase):
    id: int


class NotebookUpdate(NotebookBase):
    id: int


class NotebookDelete(NotebookBase):
    id: int
