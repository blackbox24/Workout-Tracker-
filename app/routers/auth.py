from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import UserCreate, UserResponse, LoginModel
from app.database import get_db
from app.services import auth

router = APIRouter(prefix="/auth")


@router.post("/signup", response_model=UserResponse)
async def signup(user: UserCreate, db=Depends(get_db)):
    # hash password
    # validate data
    # commit change
    # return response
    result = await auth.create_user(user)
    return result


@router.post("/login")
async def login(user_data: LoginModel, db=Depends(get_db)):
    # chech if user exists
    # verify password
    # generate token
    # return response
    user = await auth.get_user_or_404(username=user_data.username, db=db)
    if not auth.verify_password(user_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 3. Generate access and refresh tokens
    tokens = await auth.generate_auth_tokens(username=user.username, email=user.email)

    # 4. Return response
    return tokens
