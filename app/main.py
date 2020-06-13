from fastapi import FastAPI

from .routers import items, users, emails

app = FastAPI()

app.include_router(
    users.router, prefix="/api/v1/users", tags=["users"],
)
app.include_router(
    items.router, prefix="/api/v1/items", tags=["items"],
)
app.include_router(
    items.router, prefix="/api/v2/items", tags=["items"],
)
app.include_router(
    emails.router, prefix="/api/v1/emails", tags=["emails"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
