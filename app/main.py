# 3rd-party
import databases
from fastapi import FastAPI

# Project
import config
from db.base import database
from notebooks.views import router as notebooks_router
from notes.views import router as notes_router

# Normal subclass
# app = FastAPI()
# With additional info:
app = FastAPI(
    title="FastAPI-Example",
    description="Example project using FastAPI",
    version=config.settings.version,
    # The openapi schema is usually served from /openapi.json
    # You can change the url or disable it with openapi_url
    # Disabling this will also disable the docs
    #openapi_url=None,
    # Swagger UI: served at /docs.
    # You can set its URL with the parameter docs_url.
    # You can disable it by setting docs_url=None.
    # docs_url=None,
    # ReDoc: served at /redoc.
    # You can set its URL with the parameter redoc_url.
    # You can disable it by setting redoc_url=None.
    # docs_url="/docs",
    redoc_url=None,
)


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
