from fastapi import FastAPI
from db import db

api = FastAPI()

# Getting all employee details 
@api.get("/")
def all_employee():
    return db


# Parameters/Argument API Employee by id
@api.get("/employee/{employee_id}")
async def employee_by_id(employee_id: str):
    return {"employee_id": employee_id}

"""
@api.get("/employee/{employee_id}")
async def employee_by_id2(employee_id: str):
    for emp_id in db:
        if (emp_id == employee_id):
            return db[employee_id]
    return {"Status":"Employee ID not matched. "}
"""

# Get Student by name
@api.get("/Students_by_name/")
async def StudentID(name: str):
    for student_id in students:
        if students[student_id]["First Name"] == name:
            return students[student_id]
    return {"Data":"Student details not found."}
"""
    
    
    
    
    