from fastapi import APIRouter, Path, Query, Depends 
from .api_models import Student, Course, Enrollment

from database import get_db
from sqlalchemy.orm import Session
from typing import List


studentRouter = APIRouter(prefix="/students", tags=["students"])

@studentRouter.get("/", response_model=List[Student])
def all_students(db: Session = Depends(get_db)):


    all_students = db.query(Student).all()



    return all_students

@studentRouter.get("/{student_id}/", response_model=Student)
def specific_student(student_id:int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    return student