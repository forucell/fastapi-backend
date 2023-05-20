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
