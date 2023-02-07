from typing import Union, Optional, Query
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BrianHand(BaseModel):
    nodeName: str
    side: str
    countFingers: int
    level: int

app = FastAPI()

@app.get('/')
def hello():
    return {"Hello": "World"}

@app.get('/')
def hello_post():
    return {"Success": "You posted"}

@app.get('/something')
def something():
    return {"Data": "Something"}

def search_person(age: Optional[int] = Query(None, title = 'Age', description = "The age to filter for"),
                  name: Optional[str] = Query(None, title = "Name", discription = "The name to filter for")):
    
    person1 = [p for p in people if p['age'] == age]
    
    
    
    

""" @app.post("/")
async def create_hand(hand: BrianHand):
    hand.nodeName = "Nata"
    hand.side = "Left"
    hand.countFingers = 11000
    hand.level = 50
    return hand

@app.get("/")
def read_hand(hand: BrianHand):
    return hand """