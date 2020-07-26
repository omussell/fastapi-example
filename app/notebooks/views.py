# Standard Library
from typing import List
from typing import Optional

# 3rd-party
import databases
from fastapi import APIRouter

# Project
from notebooks.models import *
from notebooks.service import create
from notebooks.service import delete
from notebooks.service import get
from notebooks.service import get_all
from notebooks.service import update

router = APIRouter()


@router.get("/", response_model=List[NotebookRead], tags=["notebooks"])
async def get_notebooks():
    """Summary line.

    Usage:

    ```python
    x = "gongiveittoya"
    ```

    **Parameters:**

    * **url** - *optional* Optionally give the URL.
    """
    return await get_all()


@router.get("/{notebook_id}", response_model=NotebookCreate, tags=["notebooks"])
async def get_notebook(notebook_id: int):
    return await get(notebook_id)


@router.post("/", response_model=NotebookCreate, tags=["notebooks"])
async def create_notebook(
    notebook_text: str, notebook_completed: Optional[bool] = False
):
    return await create(notebook_text, notebook_completed)


@router.put("/{notebook_id}", response_model=NotebookUpdate, tags=["notebooks"])
async def update_notebook(
    notebook_id: int, notebook_text: Optional[str], notebook_completed: Optional[bool]
):
    return await update(notebook_id, notebook_text, notebook_completed)


@router.delete("/{notebook_id}", response_model=NotebookDelete, tags=["notebooks"])
async def delete_notebook(notebook_id: int):
    return await delete(notebook_id)
