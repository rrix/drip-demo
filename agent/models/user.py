from pydantic import BaseModel

class DataSubject(BaseModel):
    name: str
    email: str
    phone: str
    validated_identity: bool = False

