from jose import jwt
from datetime import timedelta, datetime, timezone
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.schemas import UserCreate, UserResponse
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.models import User
from app.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def verify_password(plain: str, hash: str) -> bool:
    return pwd_context.verify(plain, hash)


async def get_hash(plain: str) -> str:
    return pwd_context.hash(plain)


# create user
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    hash_password = await get_hash(user.password)

    user_data = user.model_dump(exclude={"password"})
    db_user = User(**user_data, password=hash_password)

    db.add(db_user)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        # 1. Important: Always rollback on failure
        db.rollback()

        # 1. Important: Always rollback on failure
        raise HTTPException(status_code=409, detail="username or email already exists")
    return db_user


async def get_user_or_404(username: str, db: Session = Depends(get_db)) -> UserCreate:
    stmt = select(User).where(User.username == username)
    user = db.scalars(stmt).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def create_token(data: dict, expires: timedelta | None = None):
    payload = data.copy()
    now = datetime.now()
    # 2. Use UTC for consistent timing across servers
    now = datetime.now(timezone.utc)
    expire_time = now + (expires or timedelta(minutes=settings.access_token_expires))

    payload.update({"exp": expire_time})
    encoded_jwt = jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


async def generate_auth_tokens(username: str, email: str):
    access_token = create_token(
        data={"sub": username, "email": email, "type": "access"},
        expires=timedelta(minutes=settings.access_token_expires),
    )

    refresh_token = create_token(
        data={"sub": username, "email": email, "type": "access"},
        expires=timedelta(minutes=settings.access_token_expires),
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
