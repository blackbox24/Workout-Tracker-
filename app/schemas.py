from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# ========== User Schemas ==========
class Roles:
    user: str = "user"
    admin: str = "admin"


class UserCreate(BaseModel):
    first_name: str
    middle_name: Optional[str]
    last_name: str

    email: EmailStr
    password: str
    username: str
    role: Roles


class UserUpdate(BaseModel):
    first_name: str
    middle_name: Optional[str]
    last_name: str

    email: EmailStr
    username: str
    role: Roles


class PasswordChange(BaseModel):
    old_password: str
    password1: str
    password2: str


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    role: str
    created_at: datetime
