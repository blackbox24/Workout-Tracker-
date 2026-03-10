from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from models.users import LoginBody, SignUpBody

router = APIRouter(prefix="/users", tags=["Auth"])

basic = HTTPBasic()


@router.get("/who")
async def get_user(creds: HTTPBasicCredentials = Depends(basic)):
    return {"username": creds.username, "password": creds.password}


# SIGN UP
@router.post("/api/auth/register/")
def signup(body: SignUpBody):
    # Auth
    return {"message": "Sign up successful", "user": body}


# LOGIN
@router.post("/api/auth/login")
def login(body: LoginBody):
    return {"message": "Login successful", "user": ""}
