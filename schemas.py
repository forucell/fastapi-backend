from datetime import datetime
from typing import List

from pydantic import BaseModel
from pydantic.networks import EmailStr

from enums import ProfileType


class User(BaseModel):
    username: str
    email: EmailStr
    parent_id: int | None = None


class UserBase(User):
    password: str


class UserChildBase(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True


class UserDisplay(User):
    id: str
    created_time: datetime
    children: List[UserChildBase] = []

    class Config:
        orm_mode = True


class ProfileBase(BaseModel):
    type: ProfileType | None = None


class ProfileDisplay(ProfileBase):
    id: int
    user_id: int
    created_time: datetime

    class Config:
        orm_mode = True
