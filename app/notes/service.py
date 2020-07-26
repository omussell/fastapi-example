# Standard Library
from typing import List
from typing import Optional

# Project
from notes.models import *


async def get_all() -> List[Optional[Note]]:
    """Returns all Note's."""
    notes = await Note.objects.all()
    return notes


async def get(note: NoteRead) -> Optional[Note]:
    """Get a Note."""
    note = await Note.objects.get(id=note.id)
    return note


async def create(note_create: NoteCreate) -> Note:
    """Create a Note."""
    note = await Note.objects.create(
        text=note_create.text, completed=note_create.completed
    )
    return note


async def update(note_update: NoteUpdate) -> Note:
    """Update a Note."""
    note = await Note.objects.get(id=note_update.id)
    await note.update(text=note_update.text, completed=note_update.completed)
    return note


async def delete(note_id: int) -> bool:
    """Delete a Note."""
    note = await Note.objects.get(id=note_id)
    await note.delete()
    return True
