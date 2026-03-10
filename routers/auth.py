from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from models.users import LoginBody, SignUpBody

router = APIRouter(prefix="/users", tags=["Auth"])

basic = HTTPBasic()

username: str = "nelso"
password: str = "123"


@router.get("/who")
async def get_user(creds: HTTPBasicCredentials = Depends(basic)):
    if (creds.username == username) and (creds.password == password):
        return {"username": creds.username, "password": creds.password}
    raise HTTPException(status_code=401, detail="Invalid Credentials")


# SIGN UP
@router.post("/api/auth/register/")
def signup(body: SignUpBody):
    # Auth
    return {"message": "Sign up successful", "user": body}


# LOGIN
@router.post("/api/auth/login")
def login(body: LoginBody):
    return {"message": "Login successful", "user": ""}
