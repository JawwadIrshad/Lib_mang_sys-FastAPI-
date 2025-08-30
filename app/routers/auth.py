
from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_user():
    return {"msg": "Register endpoint"}

@router.post("/login")
def login_user():
    return {"msg": "Login endpoint"}
