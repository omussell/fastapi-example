# Standard Library
from typing import List
from typing import Optional

# Project
from notes.models import Note


async def get_all() -> List[Optional[Note]]:
    """Returns all Note objects

    Returns:


    """
    notes = await Note.objects.all()
    return notes


async def get(note_id: int) -> Optional[Note]:
    """
    Args:
        note_id: ID number of the Note

    Returns:
        Note
    """
    note = await Note.objects.get(id=note_id)
    return note


async def create(note_text: str, note_completed: Optional[bool]) -> Note:
    """
    Args:

    Returns:

    """
    note = await Note.objects.create(text=note_text, completed=note_completed)
    return note


async def update(
    note_id: int, note_text: Optional[str], note_completed: Optional[bool]
) -> Note:
    """
    Args:

    Returns:

    """
    note = await Note.objects.get(id=note_id)
    await note.update(text=note_text, completed=note_completed)
    return note


async def delete(note_id: int) -> Note:
    """
    Args:

    Returns:

    """
    note = await Note.objects.get(id=note_id)
    await note.delete()
    return note
