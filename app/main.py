from fastapi import FastAPI

import config

from notes.views import router as notes_router


import databases

# SQLAlchemy specific code, as with any other app
#DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(config.settings.database_url)

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


# app.include_router(
#    cars_router, prefix="/api/v1/cars", tags=["cars"],
# )
# app.include_router(
#    cars_router, prefix="/api/v2/cars", tags=["cars"],
# )
