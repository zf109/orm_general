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

Base = declarative_base()

from ..config import Config as conf

_SCHEMA_NAME = conf.SCHEMA_TYPE

from .general import *


_employee_product_bridge = Table('employee_product_bridge', Base.metadata,
    Column('employee_id', Integer, ForeignKey(_SCHEMA_NAME + '.employee.id')),
    Column('product_id', Integer, ForeignKey(_SCHEMA_NAME + '.product.id')), schema=_SCHEMA_NAME)


class Engineer(Employee):
    __table_args__ = {"schema": _SCHEMA_NAME}
    __tablename__ = 'engineer'
    id = Column(Integer, ForeignKey(_SCHEMA_NAME+'.employee.id'), primary_key=True)
    specialty = Column(String(50))
    
    __mapper_args__ = {
        'polymorphic_identity':'engineer',
    }


class Product(Base):
    __table_args__ = {"schema": _SCHEMA_NAME}
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    value = Column(Float)
    developed_by = relationship('Employee', secondary=_employee_product_bridge)


