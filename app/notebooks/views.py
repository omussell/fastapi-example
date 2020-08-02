# Standard Library
from typing import List
from typing import Optional

# 3rd-party
import databases
from fastapi import APIRouter

# Project
from notebooks.models import *
from notebooks.service import *

router = APIRouter()


@router.get("/", tags=["notebooks"])
async def get_notebooks() -> List[NotebookRead]:
    """Get a list of Notebook's."""
    return await get_all()


@router.get("/{notebook_id}", tags=["notebooks"])
async def get_notebook(notebook: NotebookRead):
    """Get a specific notebook."""
    return await get(notebook)


@router.post("/", tags=["notebooks"])
async def create_notebook(notebook: NotebookCreate):
    """Create a Notebook."""
    return await create(notebook)


@router.put("/{notebook_id}", tags=["notebooks"])
async def update_notebook(notebook: NotebookUpdate):
    """Update a Notebook."""
    return await update(notebook)


@router.delete("/{notebook_id}", tags=["notebooks"])
async def delete_notebook(notebook_id: int):
    """Delete a Notebook."""
    return await delete(notebook_id)
