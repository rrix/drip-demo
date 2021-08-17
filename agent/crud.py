from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import agent.models as models
import agent.entities as entities
import agent.action 

import common.enums as enums

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

def get_all_data_subjects(db: Session = None,
                          skip: int = 0, limit: int = 100):
    return db.query(models.DataSubject).offset(skip).limit(limit).all()

async def create_action(db: Session = None,
                  subject_id: int = 0, business_name: str = "",
                  authority: str = "", action_type: enums.ActionType = enums.ActionType.access):
    business = db.query(models.Business) \
                 .filter(models.Business.name == business_name).limit(1).one()
    if business is None:
        raise Exception("business not found") 

    action = models.Action(
        subject_id = subject_id,
        business_id = business.id,
        authority = authority,
        state = enums.ActionState.pending
    )
    db.add(action)
    db.commit()
    db.refresh(action)
    return await agent.action.push_forward(action)
