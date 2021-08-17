from pydantic import BaseModel

class BusinessEntity(BaseModel):
    name: str
    url: str
    api_base: str

    class Config:
        orm_model = True

def FacebookEntity():
    return BusinessEntity(
        name="Facebook",
        url="https://facebook.com",
        api_base="http://localhost:5001/facebook"
    )
