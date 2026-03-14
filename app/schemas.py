from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime
from typing import Optional
from enum import Enum


# ========== User Schemas ==========
class Roles(str, Enum):
    user = "user"
    admin = "admin"


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


class LoginModel(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
