# Standard Library
from typing import List
from typing import Optional

# Project
from notebooks.models import Notebook


async def get_all() -> List[Optional[Notebook]]:
    notebooks = await Notebook.objects.all()
    return notebooks


async def get(notebook_id: int) -> Optional[Notebook]:
    notebook = await Notebook.objects.get(id=notebook_id)
    return notebook


async def create(notebook_name: str) -> Notebook:
    notebook = await Notebook.objects.create(name=notebook_name)
    return notebook


async def update(notebook_id: int, notebook_name: Optional[str]) -> Notebook:
    notebook = await Notebook.objects.get(id=notebook_id)
    await notebook.update(text=notebook_name)
    return notebook


async def delete(notebook_id: int) -> Notebook:
    notebook = await Notebook.objects.get(id=notebook_id)
    await notebook.delete()
    return notebook
