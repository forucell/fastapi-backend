from sqlalchemy.orm.session import Session

from db.models import DbStudent
from schemas import StudentBase


def create_student(db: Session, request: StudentBase):
    new_student = DbStudent(
        name=request.name,
        email=request.email,
        age=request.age
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    print(new_student.id)
    print(new_student.name)
    print(new_student.email)
    print(new_student.age)
    print(new_student.created_time)
    return new_student


def get_all_students(db: Session):
    return db.query(DbStudent).all()
