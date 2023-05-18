from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    created_time: datetime
    updated_time: datetime | None = None


    class Config:
        orm_mode = True
