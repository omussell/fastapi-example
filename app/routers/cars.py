from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/")
async def read_cars():
    return [{"name": "Car Foo"}, {"name": "Car Bar"}]


@router.get("/{car_id}")
async def read_item(car_id: int):
    return {"name": "Fake Specific Car", "car_id": car_id}
