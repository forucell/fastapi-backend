from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from db.models import DbProfile
from schemas import ProfileBase


def create_profile(db: Session, request: ProfileBase, user_id: int):
    new_profile = DbProfile(
        type=request.type,
        user_id=user_id
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile


def update_content(db: Session, id: int, request: ProfileBase):
    content = db.query(DbProfile).filter(DbProfile.id == id)
    if not content.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    content.update({
        DbProfile.type: request.type
    })
    db.commit()
    return '200'


def get_all_profiles(db: Session):
    return db.query(DbProfile).all()
