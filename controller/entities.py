from pydantic import BaseModel
from typing import Optional
from datetime import date

import common.enums


class DataSubjectResponse(BaseModel):
    dispensation: str
    response_timestamp: date
    response_expires: date
    response_url: str


class DataSubjectStatus(BaseModel):
    request_id: str
    atype: common.enums.ActionType
    status: common.enums.ActionState
    response: DataSubjectResponse
    
