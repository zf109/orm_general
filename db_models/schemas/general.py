from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import Binary
from sqlalchemy import LargeBinary
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.orm import deferred
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declarative_base
from ..config import Config as conf


_SCHEMA_NAME = conf.SCHEMA_TYPE
Base = declarative_base()

class Company(Base):
    __table_args__ = {"schema": _SCHEMA_NAME}
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    industry = Column(String(50))
    employees = relationship("Employee", back_populates="company")


class Employee(Base):
    __table_args__ = {"schema": _SCHEMA_NAME}
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    grade = Column(String(50))
    age = Column(String(50))
    type = Column(String(50))
    company_id = Column(ForeignKey(_SCHEMA_NAME+'.company.id'))
    company = relationship("Company", back_populates="employees")

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
        'polymorphic_on':type
    }


class Manager(Employee):
    __table_args__ = {"schema": _SCHEMA_NAME}
    __tablename__ = 'manager'
    id = Column(Integer, ForeignKey(_SCHEMA_NAME+'.employee.id'), primary_key=True)
    industry = Column(String(50))
    __mapper_args__ = {
        'polymorphic_identity':'manager',
    }

