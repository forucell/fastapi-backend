from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.types import Enum

from db.database import Base
from enums import ProfileType


class DbTime(Base):
    __abstract__ = True
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, onupdate=datetime.now)


class DbBase(DbTime):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)


class DbUser(DbBase):
    __tablename__ = 'user'
    username = Column(String)
    email = Column(String)
    password = Column(String)

    parent_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    children = relationship("DbUser")

    profiles = relationship('DbProfile', back_populates='user')


class DbProfile(DbBase):
    __tablename__ = 'profile'

    type = Column(Enum(ProfileType), default=ProfileType.BASIC)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("DbUser", back_populates='profiles')
