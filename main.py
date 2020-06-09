from fastapi import FastAPI
from pydantic import BaseModel, validator

# Normal subclass
# app = FastAPI()
# With additional info:
app = FastAPI(
    title="My Cool Project",
    description="This project will be cool",
    # maybe this version could be generated from gitpython?
    version="1.0.0",
    # The openapi schema is usually served from /openapi.json
    # You can change the url or disable it with openapi_url
    openapi_url=None,
    # Swagger UI: served at /docs.
    # You can set its URL with the parameter docs_url.
    # You can disable it by setting docs_url=None.
    # ReDoc: served at /redoc.
    # You can set its URL with the parameter redoc_url.
    # You can disable it by setting redoc_url=None.
    docs_url="/docs",
    redoc_url=None,
)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"We expect price >= 0, we received {value}")
        return value


@app.get("/items/{item_id}", tags=["items"])
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post(
    "/items/",
    response_model=Item,
    summary="summary in decorator. Lets create some items",
    response_description="description used in response in swagger UI",
    tags=["items"],
)
async def create_item(item: Item):
    """
    # Example documentation

    Create items that are super cool

    This docstring is added as documentation in the swagger UI for this function. It renders markdown so you can do things like **bold**.

    Response model = [response_model](https://fastapi.tiangolo.com/tutorial/response-model/)

    The summary is usually just the function name with `_` replaced with spaces and each word capitalised. But you can override it with the summary parameter.

    response_description is used to document the response in the swagger UI

    Tags group these functions together in the swagger UI
    """
    return item
