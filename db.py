from uuid import uuid4
from typing import List
from validators import *

db: List[User] = [
    User(
        id=uuid4(), 
        first_name = "Ranjan",
        last_name = "Kumar",
        gender = Gender.MALE,
        role = Role.deve,
        ),
    User(
        id = uuid4(),
        first_name = "Arpit",
        last_name = "Jain",
        gender = Gender.MALE,
        role = Role.admin,
        ),
    User(
        id = uuid4(),
        first_name = "Soni",
        last_name = "Kumari",
        gender = Gender.FEMALE,
        role = Role.student
    )
]