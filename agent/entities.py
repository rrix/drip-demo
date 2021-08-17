from pydantic import BaseModel
from typing import Optional

import common.enums


class DataSubject(BaseModel):
    name: str
    email: str
    phone: str
    validated_identity: bool = False

    class Config:
        orm_model = True


class Action(BaseModel):
    subject_id: int
    business_id: str
    authority: str
    external_id: Optional[str]
    state: common.enums.ActionState
    atype: common.enums.ActionType

    class Config:
        orm_model = True


class Business(BaseModel):
    name: str
    url: str
    api_base: str

    class Config:
        orm_model = True
