from fastapi import APIRouter

router=APIRouter(
    prefix="/user",tags=["Users"])

@router.get("/all")          #  Static Route 
def get_all_users():           #  Always Define the the Static Route before the Dynamic Route
    return "All Users"    

# Path Parameter
@router.get("/{username}")   #Dynamic Route
def get_user(username:str):
    return {f"User profile for {username}"}

@router.get("/{username}/post/{post_id}")
def get_user(username:str,post_id:int):
    return {f"Post {post_id} is posted by {username}"}
 