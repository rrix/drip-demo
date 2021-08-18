from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session 

import common.enums as enums

import common.entities as centities
import controller.entities as entities

from controller.database import SessionLocal, engine
import controller.models as models
import controller.crud as crud

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def insert_business_entities(db: Session):
    fb = centities.FacebookEntity()
    biz = models.Business(
        name = fb.name,
        url = fb.url,
        api_base = fb.api_base
    )
    db.add(biz)
    db.commit()
    db.refresh(biz)
    return biz

def get_app():
    insert_business_entities(SessionLocal())
    return app

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return db.query(DataSubject).all()

@app.post("/{controller}/excercise")
async def new_exercise(req: centities.DataSubjectRequest,
                       db: Session = Depends(get_db)):
    return crud.persist_exercise(db, req)

@app.get("/{controller}/status",
         response_model_exclude_unset=True,
         response_model=entities.DataSubjectStatus)
async def exercise_status(request_id: str,
                          db: Session = Depends(get_db)):
    return crud.exercise_status(db, request_id)
