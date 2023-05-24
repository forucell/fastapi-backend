from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db import db_student
from db.database import get_db
from schemas import StudentBase, StudentDisplay, UserBase

router = APIRouter(
    prefix='/student',
    tags=['student']
)


# Create student
@router.post('/')
def create_student(request: StudentBase, db: Session = Depends(get_db)):
    return db_student.create_student(db, request)


@router.get('/', response_model=List[StudentDisplay])
def get_all_students(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_student.get_all_students(db)
