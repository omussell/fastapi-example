from fastapi import FastAPI

from .routers import drivers, cars, trips

app = FastAPI()

app.include_router(
    drivers.router, prefix="/api/v1/drivers", tags=["drivers"],
)
app.include_router(
    cars.router, prefix="/api/v1/cars", tags=["cars"],
)
app.include_router(
    cars.router, prefix="/api/v2/cars", tags=["cars"],
)
app.include_router(
    trips.router, prefix="/api/v1/trips", tags=["trips"],
)


# @app.on_event("startup")
# async def startup():
#    await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#    await database.disconnect()
