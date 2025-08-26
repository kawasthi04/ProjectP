from pydantic import BaseModel
from datetime import date
from typing import Optional

class StudentBase(BaseModel):
    name: str
    usn: str
    college_email: str
    personal_email: str
    dob: date
    tenth_marks: float
    twelfth_marks: float
    cgpa: float
    backlog_status: bool
    department_id: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    college_email: Optional[str] = None
    personal_email: Optional[str] = None
    cgpa: Optional[float] = None

class Student(StudentBase):
    id: int
    class Config:
        from_attributes = True
