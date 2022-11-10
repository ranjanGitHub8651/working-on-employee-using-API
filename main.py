from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from db import db
from typing import List
from validators import *
from uuid import UUID

api = FastAPI()


@api.get("/users/")
def all_user():
    return db


@api.get("/user/{user_id}/")
async def user_by_id(user_id: UUID):
    for user_obj in db:
        if (user_obj.id == user_id):
            return user_obj
    raise HTTPException(status_code=404, detail="User ID not found.")


@api.post("/user/")
async def insert_user(user: User):
    db.append(user)
    return user


@api.patch("/user/{user_id}/")
async def user_update(user_id: UUID, user: UpdateUser):
    print(user_id)
    for user_obj in db:
        print(user_obj.id)
        if user_obj.id == user_id:
            print("*************************")
            data = user_obj.dict()
            user_model = User(**data)
            print(user_model)
            
            update_data = user.dict(exclude_unset=True)
            print(update_data)
            
            update_user = user_model.copy(update=update_data)
            user_obj = jsonable_encoder(update_user)
            print(user_obj)
            db.append(User(**user_obj))
            return user_obj
        else:    
            raise HTTPException(status_code=404, detail="User ID not exist.")
    


# @api.delete("/user/{user_id}/")
# async def delete_user(user_id: str):
#     if(user_id not in User):
#         raise HTTPException(status_code=403, detail="Error in deleteing. ")
#     del User[user_id]
#     return {"Message": "User deleted successfully."}
