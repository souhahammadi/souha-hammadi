from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, database

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"message": "Hello DB API"}