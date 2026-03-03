from fastapi import APIRouter
from models.users import LoginBody, SignUpBody

router = APIRouter(prefix="users", tags=["users"])


# SIGN UP
@router.post("/api/auth/register/")
def signup(body: SignUpBody):
    # Auth
    return {"message": "Sign up successful", "user": body}


# LOGIN
@router.post("/api/auth/login")
def login(body: LoginBody):
    return {"message": "Login successful", "user": ""}
