from typing import Optional
from sqlmodel import SQLModel, Field


#class Hero(SQLModel, table=True):
#    id: Optional[int] = Field(default=None, primary_key=True)
#    name: str = Field(index=True)
#    secret_name: str
#    age: Optional[int] = Field(default=None, index=True)

#class Plant(SQLModel, table=True):
#    id: Optional[int] = Field(default=None, primary_key=True)
#    name: str


class PlantBase(SQLModel):
    name: str = Field(index=True)
    age: Optional[int] = Field(default=None, index=True)

class Plant(PlantBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class PlantCreate(PlantBase):
    pass

class PlantRead(PlantBase):
    id: int

class PlantUpdate(SQLModel):
    name: Optional[str] = None
    age: Optional[int] = None
