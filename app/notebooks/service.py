# Standard Library
from typing import List
from typing import Optional

# Project
from notebooks.models import *


async def get_all() -> List[Optional[Notebook]]:
    """Returns all Notebook's."""
    notebooks = await Notebook.objects.all()
    return notebooks


async def get(notebook: NotebookRead) -> Optional[Notebook]:
    """Get a Notebook."""
    notebook = await Notebook.objects.get(id=notebook.id)
    return notebook


async def create(notebook_create: NotebookCreate) -> Notebook:
    """Create a Notebook."""
    notebook = await Notebook.objects.create(name=notebook_create.name)
    return notebook


async def update(notebook_update: NotebookUpdate) -> Notebook:
    """Update a Notebook."""
    notebook = await Notebook.objects.get(id=notebook_update.id)
    await notebook.update(name=notebook_update.name)
    return notebook


async def delete(notebook_id: int) -> bool:
    """Delete a Notebook."""
    notebook = await Notebook.objects.get(id=notebook_id)
    await notebook.delete()
    return True
