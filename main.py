from fastapi import FastAPI, HTTPException
from starlette import status
from models.db import db
from models.models import Sheep
from typing import List

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    return db.get_sheep(id)

@app.get("/sheep", response_model=List[Sheep])
def read_all_sheep():
    return db.read_all_sheep()

@app.post("/sheep", response_model=Sheep, status_code= status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")
    db.data[sheep.id] = sheep
    return sheep

@app.put("/sheep/{id}", response_model=Sheep)
def update_sheep(id: int, sheep: Sheep):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep not found")
    sheep.id = id
    db.data[id] = sheep
    return sheep

@app.delete("/sheep/{id}", response_model=Sheep)
def delete_sheep(id: int):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep not found")
    sheep = db.delete_sheep(id)
    return sheep

