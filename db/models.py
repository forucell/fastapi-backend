from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime

from db.database import Base
from datetime import datetime

class DbBase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, onupdate=datetime.now)


class DbUser(DbBase):
    __tablename__ = 'user'
    username = Column(String)
    email = Column(String)
    password = Column(String)
