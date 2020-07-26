# Standard Library
from typing import List
from typing import Optional

# 3rd-party
import databases
from fastapi import APIRouter

# Project
from notes.models import *
from notes.service import *

router = APIRouter()


@router.get("/", tags=["notes"])
async def get_notes() -> List[NoteRead]:
    """Get a list of Note's."""
    return await get_all()


@router.get("/{note_id}", tags=["notes"])
async def get_note(note: NoteRead):
    """Get a specific note."""
    return await get(note)


@router.post("/", tags=["notes"])
async def create_note(note: NoteCreate):
    """Create a Note."""
    return await create(note)


@router.put("/{note_id}", tags=["notes"])
async def update_note(note: NoteUpdate):
    """Update a Note."""
    return await update(note)


@router.delete("/{note_id}", tags=["notes"])
async def delete_note(note_id: int):
    """Delete a Note."""
    return await delete(note_id)
