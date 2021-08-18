import uuid
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import controller.models as models
import controller.entities as entities

import common.enums as enums
import common.entities as centities
import controller.entities as entities

def new_data_subject(sub: centities.DataSubject):
    model_subject = models.DataSubject(
        name = sub.name,
        email = sub.email,
        phone = sub.phone,
        userid = sub.userid
    )
    return model_subject

def persist_exercise(db: Session, req: centities.DataSubjectRequest):
    # don't forget to persist this!
    subject = new_data_subject(req.subject)
    controller = db.query(models.Business) \
                   .filter(models.Business.name == req.controller.name) \
                   .all()[0]

    if subject is None:
        raise Exception("could not make subject")
    if controller is None:
        raise Exception("could not find controller")

    # give 'em an ID, maybe you can comment this out, i'd rather not have to COMMIT though
    db.add(subject)
    
    model_obj = models.DataSubjectRequest(
        subject=subject,
        business=controller,

        atype=req.request_type,
        state=enums.ActionState.opened,

        external_id=uuid.uuid4().hex,
        authority=req.request_authority,

        # expires_at = Arrow.now().shift('7days')
        created_at=datetime.now()
    )
    db.add(model_obj)
    db.commit()
    db.refresh(model_obj)
    return model_obj

def exercise_status(db: Session, external_id: str):
    model = db.query(models.DataSubjectRequest) \
             .filter(models.DataSubjectRequest.external_id == external_id) \
             .one()

    ent = entities.DataSubjectStatus(
        request_id=model.external_id,
        request_type=model.atype,
        status=model.state
    )

    if ent.status.is_closed():
        ent.response = make_response_data(model)

    return ent

def make_response_data(status: models.DataSubjectRequest):
    return entities.DataSubjectResponse(
        dispensation=model.dispensation,
        response_url=model.response_url,
        response_timestamp=model.created_at,
        response_expires=model.expirs_at
    )
