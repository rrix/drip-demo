from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import agent.models as models
import agent.entities as entities
import agent.crud as crud

from agent.database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_app():
    return app

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return db.query(DataSubject).all()

@app.put("/data_subject")
def put_data_subject(sub: entities.DataSubject,
                     db: Session = Depends(get_db)):
    return crud.create_subject(db, sub)

@app.get("/data_subjects")
def get_all_data_subjects(skip: int = 0, limit: int = 100,
                          db: Session = Depends(get_db)):
    return crud.get_all_data_subjects(db, skip, limit)
