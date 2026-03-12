from models.users import UserBase
from fastapi import HTTPException

fakes = [
    UserBase(first_name="john", last_name="doe", role="user", username="johndoe12"),
    UserBase(first_name="john1", last_name="doe2", role="user", username="johndoe112"),
]


def find(username: str) -> UserBase | None:
    for e in fakes:
        if e.username == username:
            return e
    return None


def checking_missing(username: str):
    if not find(username):
        raise HTTPException(detail="User not found", status_code=404)


def check_duplicate(username: str):
    if find(username):
        raise HTTPException(detail="User already exists", status_code=401)


def get_all() -> list[UserBase]:
    return fakes


def get_one(username: str) -> UserBase | None:
    checking_missing(username)
    return find(username)


def create(user: UserBase) -> UserBase:
    check_duplicate(user.username)
    fakes.append(user)
    return user


def modify(user: UserBase, username: str) -> UserBase:
    checking_missing(username)
    for e in range(0, len(fakes)):
        if fakes[e].username == username:
            fakes[e] = user
            break
    return user


def delete(username: str) -> None:
    checking_missing(username)
    for e in range(0, len(fakes)):
        if fakes[e].username == username:
            fakes.remove(fakes[e])
            break

    return None
