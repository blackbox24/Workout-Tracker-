from pydantic import Field, BaseModel
from enum import Enum


class Roles(Enum):
    user = "user"
    admin = "admin"


class UserBase(BaseModel):
    first_name: str = Field(max_length=20)
    middle_name: str | None = Field(max_length=20)
    last_name: str = Field(max_length=20)
    role: str | Roles = Field(max_length=20)
    username: str = Field(max_length=20)


class PasswordModel(BaseModel):
    password1: str = Field(max_length=16, min_length=8)
    password2: str = Field(max_length=16, min_length=8)


class UserUpdate(UserBase):
    pass


class UserUpdatePassword(PasswordModel):
    old_password: str = Field(max_length=16, min_length=8)


class UserResponse(UserBase):
    pass


class SignUpBody(UserBase, PasswordModel):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "John",
                    "middle_name": "",
                    "last_name": "Doe",
                    "username": "johndoe12",
                    "password": "Pass@word123",
                    "role": "user",
                }
            ]
        }
    }


class LoginBody(BaseModel):
    username: str = Field(max_length=20)
    password1: str = Field(max_length=16, min_length=8)


class LoginResponse(UserBase):
    access_token: str
    refresh_token: str
