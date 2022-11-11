from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class Role(str, Enum):
    admin = "Admin"
    user = "User"
    student = "Student"
    deve = "Developer"
    
class User(BaseModel):
    id: UUID | None = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    role: Role

class UpdateUser(BaseModel):
    first_name: str 
    last_name: str | None
    gender: Gender
    role: Role