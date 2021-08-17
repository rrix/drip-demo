from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date

from controller.database import Base


class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    requests = relationship("DataSubjectRequest", viewonly=True)
    name = Column(String)
    url = Column(String)
    api_base = Column(String)


class DataSubject(Base):
    __tablename__ = "data_subjects"

    id = Column(Integer, primary_key=True, index=True)
    requests = relationship("DataSubjectRequest", viewonly=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    userid = Column(String)


class DataSubjectRequest(Base):
    __tablename__ = "data_subject_request"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey('data_subjects.id'))
    business_id = Column(Integer, ForeignKey('businesses.id'))

    state = Column(String)
    atype = Column(String)
    authority = Column(String)
    external_id = Column(String)

    business = relationship(Business)
    subject = relationship(DataSubject)
