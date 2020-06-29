from fastapi import FastAPI

from drivers.views import router as drivers_router

import databases

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

app = FastAPI()

app.include_router(
    drivers_router, prefix="/api/v1/drivers", tags=["drivers"],
)


# app.include_router(
#    cars_router, prefix="/api/v1/cars", tags=["cars"],
# )
# app.include_router(
#    cars_router, prefix="/api/v2/cars", tags=["cars"],
# )


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
