from sqlalchemy import Column, Integer, String, Numeric, Boolean, Date, ForeignKey
from .database import Base

class Department(Base):
    __tablename__ = "departments"
    department_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    usn = Column(String, unique=True, nullable=False)
    college_email = Column(String, nullable=False)
    personal_email = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    tenth_marks = Column(Numeric, nullable=False)
    twelfth_marks = Column(Numeric, nullable=False)
    cgpa = Column(Numeric, nullable=False)
    backlog_status = Column(Boolean, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.department_id"), nullable=False)
