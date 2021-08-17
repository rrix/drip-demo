from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from typing import Optional

class BusinessEntity(BaseModel):
    name: str
    url: str
    api_base: Optional[str]

    class Config:
        orm_model = True

def FacebookEntity():
    return BusinessEntity(
        name="Facebook",
        url="https://facebook.com",
        api_base="http://localhost:5001/facebook"
    )

class DataSubject(BaseModel):
    name: str
    email: str
    phone: str
    userid: str


class DataSubjectRequest(BaseModel):
    controller: BusinessEntity
    subject: DataSubject
    request_authority: str
    request_type: str
