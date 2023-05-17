from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.hash import bcrypt
from db.models import DbUser
from schemas import UserBase


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: bcrypt(request.password)
    })
    db.commit()
    return '200'


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found')
    return user


def get_all_users(db: Session):
    return db.query(DbUser).all()
