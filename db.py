from uuid import uuid4
from typing import List
from validators import *

db: List[User] = [
    User(
        #id=uuid4(),
        id = "d9c3e758-a301-433b-948e-bdaef21426d7", 
        first_name = "Ranjan",
        last_name = "Kumar",
        gender = Gender.MALE,
        role = Role.deve,
        ),
    User(
        id = "bc3517ef-1247-4f25-858e-6d524d8b4fef",
        first_name = "Arpit",
        last_name = "Jain",
        gender = Gender.MALE,
        role = Role.admin,
        ),
    User(
        id = "18c8707a-6b62-4742-a5bb-ee9290f72811",
        first_name = "Soni",
        last_name = "Kumari",
        gender = Gender.FEMALE,
        role = Role.student
    )
]