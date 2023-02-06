from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Brian(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Wellcome to": "Brian Core!", 
            "none":"none"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}