# Standard Library
from typing import List
from typing import Optional

# Project
from notes.models import Note


async def get_all() -> List[Optional[Note]]:
    notes = await Note.objects.all()
    return notes


async def get(note_id: int) -> Optional[Note]:
    note = await Note.objects.get(id=note_id)
    return note


async def create(note_text: str, note_completed: Optional[bool]) -> Note:
    note = await Note.objects.create(text=note_text, completed=note_completed)
    return note


async def update(note_id: int, note_text: Optional[str], note_completed: Optional[bool]) -> Note:
    note = await Note.objects.get(id=note_id)
    await note.update(text=note_text, completed=note_completed)
    return note


async def delete(note_id: int) -> Note:
    note = await Note.objects.get(id=note_id)
    await note.delete()
    return note
