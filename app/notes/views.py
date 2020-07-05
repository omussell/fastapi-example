# Standard Library
from typing import List, Optional

# Project
import databases
# import notes.models
from notes.models import *
from notes.service import get_all
from fastapi import APIRouter
#from config import *

# SQLAlchemy specific code, as with any other app
#DATABASE_URL = "sqlite:///./sqlite.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

#database = databases.Database(DATABASE_URL)


router = APIRouter()


#@router.get("/", response_model=List[NoteBase], tags=["notes"])
@router.get("/", tags=["notes"])
async def get_notes(description: Optional[str] = None):
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
    #notes = Note.__table__.select()
    #return await database.fetch_all(notes)
    return await get_all()


@router.get("/{note_id}", response_model=NoteBase, tags=["notes"])
async def get_note(note_id: int):
    # return {"note": note_id}
    return await database.fetch(Note)

@router.post("/", response_model=NoteBase, tags=["notes"])
async def create_note(description: str = None):
    return False


@router.put("/{note_id}", response_model=NoteBase, tags=["notes"])
async def update_note(description: str = None):
    return False

@router.delete("/{note_id}", response_model=NoteBase, tags=["notes"])
async def update_note(description: str = None):
    return False
