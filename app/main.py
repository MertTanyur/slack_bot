from typing import Optional

from fastapi import FastAPI, Request, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://127.0.0.1:8000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class Req(BaseModel):
    at: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/subscription")
def subscribe():
    print('adf')
    return {'at': 'asdlfkj'}


@app.post("/trial/")
def subscribe(req: Request):
    print(req)
    print('patates')
    return req


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.post("/dummypath")
async def get_body(request: Request):
    return await request.json()


@app.post('/test')
async def update_item(
        payload: dict = Body(...)
):
    return payload


@app.post('/test2')
async def update_item(
        payload: dict = Body(...), response_model=str
):
    return payload.challenge


@app.post('/test3')
async def update_item(
        payload: dict = Body(...),
):
    return payload.challenge
