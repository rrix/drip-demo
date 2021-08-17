from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date

from agent.database import Base


class DataSubject(Base):
    __tablename__ = "data_subjects"

    id    = Column(Integer, primary_key=True, index=True)
    name  = Column(String)
    email = Column(String)
    phone = Column(String)
    validated_identity = Column(Boolean)


class Action(Base):
    __tablename__ = "authorized_action"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey('data_subjects.id'))
    business_id = Column(Integer, ForeignKey('businesses.id'))

    state = Column(String)
    atype = Column(String)
    authority = Column(String)
    external_id = Column(String)


class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    actions = relationship(Action)
    name = Column(String)
    url = Column(String)
    api_base = Column(String)
