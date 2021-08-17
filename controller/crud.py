from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import controller.models as models
import controller.entities as entities

import common.enums as enums
import common.entities as centities
import controller.entities as entities

def persist_data_subject(db: Session, sub: centities.DataSubject):
    model_subject = models.DataSubject(
        name = sub.name,
        email = sub.email,
        phone = sub.phone,
        userid = sub.userid
    )
    db.add(model_subject)
    db.commit()
    db.refresh(model_subject)
    return model_subject

def persist_exercise(db: Session, req: centities.DataSubjectRequest):
    subject = persist_data_subject(db, req.subject)
    controller = db.query(models.Business).filter(models.Business.name == req.controller.name)
    
