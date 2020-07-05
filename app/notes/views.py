# Standard Library
from typing import List

# Project
import databases
# import notes.models
from notes.models import *
from fastapi import APIRouter

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./sqlite.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)


router = APIRouter()


@router.get("/", response_model=List[NoteBase], tags=["notes"])
async def read_notes(url: str = None):
    """
    Summary line

    Usage:

    ```python
    x = "gongiveittoya"
    ```

    **Parameters:**

    * **url** - *optional* Optionally give the URL.
    """
    # return [{"username": "Foo"}, {"username": "Bar"}]
    notes = Note.__table__.select()
    return await database.fetch_all(notes)


@router.get("/{note_id}", response_model=NoteBase, tags=["notes"])
async def read_note(note_id: int):
    # return {"note": note_id}
    return await database.fetch(Note)
