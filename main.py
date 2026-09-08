from fastapi import FastAPI, Path, Query
from typing import Optional
from enum import Enum
from backend.students.routes import studentRouter
from backend.students.database_models import StudentDB, CourseDB
from database import Base, engine



app = FastAPI() 

app.include_router(studentRouter)




#Create tables in the database if they don't exist
Base.metadata.create_all(bind=engine)