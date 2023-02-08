from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

# Structure of The Hand Object
hands = {
    1: {
        "name": "Natanael",
        "side": "Left",
        "countFingers": 10011,
        "level": 100
    }
}

# Obj to create new Hands
class CreateHand(BaseModel):
    name: str
    side: str
    countFingers: int
    level: int
 
# Obj to update new Hands    
class UpdateHand(BaseModel):
    name: Optional[str] = None
    side: Optional[str] = None
    countFingers: Optional[int] = None
    level: Optional[int] = None
    
# Show all hands in API    
@app.get('/')
def index():
    return hands

# Get hand by id
@app.get('/hand/{hand_id}')
def get_hand_id(hand_id: int = Path(None, description = "The id of the hand you want to view")):

    return hands[hand_id]


# Get hand by name
@app.get('/get-hand-by-name/{name}')
def get_hand_name(name: Optional[str] = None):
    
    for hand_id in hands:
        if hand_id == 1 and name  == hands[hand_id]["name"]:
            return hands[hand_id]
        if hand_id > 1 and name  == hands[hand_id].name:
            return hands[hand_id]
        
    return {"Data": "Not Found"}
   
   
# Create a new hand    
@app.post("/create-hand/{hand_id}")
def creat_hand(hand_id: int, hand: CreateHand):
    
    if hand_id in hands:
        return {"Error": "Hand exists"}
    
    hands[hand_id] = hand
    return hands[hand_id]
    
    
# Update fields    
@app.put('/update-hand/{hand_id}')
def update_hand(hand_id: int, hand: UpdateHand):
    
    if hand_id > 1:
        if hand_id not in hands: 
            return {"Error": "Hand does not exist"} 
        
        if hand.name != None:
            hands[hand_id].name = hand.name
            
        if hand.side != None:
            hands[hand_id].side = hand.side
            
        if hand.countFingers != None:
            hands[hand_id].countFingers = hand.countFingers
            
        if hand.level != None:
            hands[hand_id].level = hand.level
    else:
        if hand_id not in hands: 
            return {"Error": "Hand does not exist"} 
        
        if hand.name != None:
            hands[hand_id]["name"] = hand.name
            
        if hand.side != None:
            hands[hand_id]["side"] = hand.side
            
        if hand.countFingers != None:
            hands[hand_id]["countFingers"] = hand.countFingers
            
        if hand.level != None:
            hands[hand_id]["level"] = hand.level
          
    return hands[hand_id]
  
    
# Delete hand by id
@app.delete("/delete-hand/{hand_id}")
def delete_hand(hand_id: int):
    
    if hand_id not in hands:
        return {"Error": "Hand does not exist"}
    
    del hands[hand_id]
    return {"Message": "Hand Deleted successfully"}