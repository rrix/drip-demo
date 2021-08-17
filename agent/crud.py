from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import agent.models as models
import agent.entities as entities

def create_subject(db: Session, user: entities.DataSubject):
    db_user = models.DataSubject(
        name = user.name,
        email = user.email,
        phone = user.phone,
        validated_identity = True # XXX this should eventually go through a user-flow
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_data_subjects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DataSubject).offset(skip).limit(limit).all()
