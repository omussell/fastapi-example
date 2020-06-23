from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["drivers"])
async def read_drivers():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.get("/{driver_id}", tags=["drivers"])
async def read_user(driver_id: int):
    return {"driver": driver_id}
