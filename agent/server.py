from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import agent.models as models
import agent.crud as crud
import agent.entities as entities

import common.enums as enums
import common.entities as centities

from agent.database import SessionLocal, engine


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

@app.put("/data_subject")
def put_data_subject(sub: entities.DataSubject,
                     db: Session = Depends(get_db)):
    return crud.create_subject(db, sub)

@app.get("/data_subjects")
def get_all_data_subjects(db: Session = Depends(get_db),
                          skip: int = 0, limit: int = 100):
    return crud.get_all_data_subjects(db, skip, limit)

@app.post("/excercise")
async def new_authorized_action(db: Session = Depends(get_db),
                          subject_id: int = 0, business_name: str = "",
                          authority: str = "", action_type: enums.ActionType = enums.ActionType.access):
    return await crud.create_action(db, subject_id, business_name, authority, action_type)
