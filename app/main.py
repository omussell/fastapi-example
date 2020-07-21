# 3rd-party
import databases
from fastapi import FastAPI

# Project
import config
from db.base import database
from notes.views import router as notes_router
from notebooks.views import router as notebooks_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(
    notes_router, prefix="/api/v1/notes", tags=["notes"],
)
app.include_router(
    notebooks_router, prefix="/api/v1/notebooks", tags=["notebooks"],
)


# app.include_router(
#    cars_router, prefix="/api/v1/cars", tags=["cars"],
# )
# app.include_router(
#    cars_router, prefix="/api/v2/cars", tags=["cars"],
# )
