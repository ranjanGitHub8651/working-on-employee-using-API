from fastapi import FastAPI, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from db import db
from typing import List
from validators import *
from uuid import UUID

api = FastAPI()


@api.post("/user/")
async def insert_user(user: User):
    db.append(user)
    return user


@api.get("/users/")
def all_user():
    return db


@api.get("/user/{user_id}/")
async def user_by_id(user_id: UUID):
    for user_obj in db:
        if (user_obj.id == user_id):
            return user_obj
    raise HTTPException(status_code=404, detail="User ID not found.")


@api.patch("/user/{user_id}/")
async def user_update(user_id: UUID, user: UpdateUser):
    for user_obj in db:
        if user_obj.id == user_id:
            data = user_obj.dict()
            user_model = User(**data)
            update_data = user.dict(exclude_unset=True)
            # print(update_data)
            update_user = user_model.copy(update=update_data)
            user_obj = jsonable_encoder(update_user)
            print(user_obj)
            # db.append(User(**user_obj))
            return {"message", f"Successfully updated user: {user_obj}"}
        else:
            raise HTTPException(status_code=404, detail="User ID not exist.")


# Method 1 for delete
"""
@api.delete("/user/{user_id}/")
async def delete_user_by_id(user_id: UUID):
    cnt = 0
    for obj in db:
        cnt += 1
        if obj.id == user_id:
            del db[cnt-1]
            return {"Message": f"ID {user_id} deleted."}
    return HTTPException(status_code=404, detail="User dose not exits. ")
"""

# method 2 for delete

@api.delete("/user/{user_id}/")
async def delete_by_id(user_id: UUID = Path(None, description="Enter valid user ID")):
    del_obj = 0
    for user in db:
        del_obj += 1
        if user.id == user_id:
            db.pop(del_obj-1)
            return {"Msg": f"Delete successfully: {user_id}"}

    raise HTTPException(status_code=404, detail="User dose not exist. ")
