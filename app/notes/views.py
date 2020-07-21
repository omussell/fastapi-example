# Standard Library
from typing import List
from typing import Optional

# 3rd-party
import databases
from fastapi import APIRouter

# Project
from notes.models import *
from notes.service import create
from notes.service import delete
from notes.service import get
from notes.service import get_all
from notes.service import update

router = APIRouter()


@router.get("/", response_model=List[NoteRead], tags=["notes"])
async def get_notes():
    """
    Summary line

    Usage:

    ```python
    x = "gongiveittoya"
    ```

    **Parameters:**

    * **url** - *optional* Optionally give the URL.
    """
    return await get_all()


@router.get("/{note_id}", response_model=NoteCreate, tags=["notes"])
async def get_note(note_id: int):
    """
    Get a specific note.

    Args:
        note_id: The identifier

    Returns:
        Note: A single note
    """
    return await get(note_id)


@router.post("/", response_model=NoteCreate, tags=["notes"])
async def create_note(note_text: str, note_completed: Optional[bool] = False):
    """
    Create a note.

    Args:
        note_text: The info for the text
        note_completed: Whether or not its done

    Returns:
        Note: A single note
    """
    return await create(note_text, note_completed)


@router.put("/{note_id}", response_model=NoteUpdate, tags=["notes"])
async def update_note(note_id: int, note_text: Optional[str], note_completed: Optional[bool]):
    return await update(note_id, note_text, note_completed)


@router.delete("/{note_id}", response_model=NoteDelete, tags=["notes"])
async def delete_note(note_id: int):
    return await delete(note_id)
