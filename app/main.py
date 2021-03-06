from slack_sdk.errors import SlackApiError
from slack_sdk import WebClient
import os
import logging
from typing import Optional

from fastapi import FastAPI, Request, Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://slack-sammy.herokuapp.com/",
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


# valid
@app.post("/dummypath")
async def get_body(request: Request):
    return await request.json()

# valid


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


# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.environ.get(
    "xoxb-2992220446947-3043543216550-UH4TgUObFkg0dQcSUe6joSDc"))
logger = logging.getLogger(__name__)
channel_name = "genel"
conversation_id = None


@app.get('/messages')
def list_messages():
    response = {'conversation_id_list': []}
    try:
        print('hello world')
        # Call the conversations.list method using the WebClient
        for response in client.conversations_list():
            if conversation_id is not None:
                break
            for channel in result["channels"]:
                if channel["name"] == channel_name:
                    conversation_id = channel["id"]
                    # Print result
                    print(f"Found conversation ID: {conversation_id}")
                    response['conversation_id_list'].append(conversation_id)
                    break
        return response
    except SlackApiError as e:
        print(f"Error: {e}")
        return {'Error message': e}


@app.get('/send_message')
def send_message():
    try:
        response = client.chat_postMessage(
            channel="C0325U9F3S5",
            text="Merhabalar ben sammy!"
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["error"]
