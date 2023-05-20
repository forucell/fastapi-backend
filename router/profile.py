from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db import db_profile
from db.database import get_db
from schemas import ProfileDisplay, ProfileBase, UserBase

router = APIRouter(
    prefix='/profile',
    tags=['profile']
)


# Create profile
@router.post('/', response_model=ProfileDisplay)
def create_profile(request: ProfileBase, db: Session = Depends(get_db),
                   current_user: UserBase = Depends(get_current_user)):
    return db_profile.create_profile(db, request, current_user.id)
