import uuid
from pydantic import BaseModel



class StudentSchema(BaseModel):
    name : str
    age : int 
    department : str
    level : int
    email : str 

    model_config = {
        "from_attributes": True
    }

class CourseSchema(BaseModel):
    name : str
    code : str
    unit : int
    lecturer : str
    

class EnrollmentSchema(BaseModel):
    semester : int
    score : int

    model_config = {
        "from_attributes": True
    }