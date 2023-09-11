from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

db: Dict[int, dict] = {}

class Person(BaseModel):
    name: str
    age: str 
    email: str


@app.get("api/persons/")
async def get_persons():
    return list(db.values())

@app.post("/api/person/", response_model=Person)
async def create_person(person: Person):
    person_id = str(len(db) + 1)
    db[person_id] = person.dict()
    return person

    
@app.get("/api/person/{person_id}", response_model=Person)
async def read_person(person_id: int):
    if person_id not in db:
        raise HTTPException(status_code=404, detail="Person not found")
    return db[person_id]

    