from fastapi import HTTPException
from . import curs
from models.users import UserBase, SignUpBody, UserUpdatePassword
from typing import List
from bcrypt import checkpw, hashpw


curs.execute(
    """
    CREATE TABLE IF NOT EXIST users(
        id BIGINT GENERATED AS IDENTITY PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        middle_name VARCHAR(50),
        last_nmae VARCHAR(50) NOT NULL,
        username VARCHAR(100) UNIQUE,
        role VARCHAR(10) CHECK (role in ('user','admin')),
        password VARCHAR(100) NOT NULL,

        created_at TIMESTAMPZ DEFAULT CURRENT_TIMESTAMPZ,
        CONSTRAINT UNIQUE full_name (first_name, middle_name, last_name)
    )
    """
)


def row_to_model(row: tuple) -> UserBase:
    first_name, middle_name, last_name, username, role, others = row
    return UserBase(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        username=username,
        role=role,
    )


def model_to_dict(user: UserBase) -> dict:
    return user.model_dump()


def get_one(id: int) -> UserBase:
    stmt = """
        SELECT 
            first_name, middle_name, last_name,
            username, role
        FROM 
            users
        WHERE id=:id
    """
    params = {"id": id}
    query = curs.execute(stmt, params)
    row = query.fetchone()
    if row:
        return row_to_model(row)
    raise HTTPException(status_code=404, detail="user not found")


def get_all() -> List[UserBase]:
    stmt = """
        SELECT
            first_name, middle_name, last_name,
            username, role
        FROM 
            users
    """
    query = curs.execute(stmt)
    objs = query.fetchall()
    return [row_to_model(obj) for obj in objs]


def get_user_or_404(username: str) -> dict:
    stmt = """
    SELECT username, password
    FROM users
    WHERE username=:username
    """
    try:
        user = curs.execute(stmt, {"username": username})
        row = user.fetchone()
    except HTTPException:
        raise HTTPException(status_code=404, detail="User not found")

    return row


def create_user(user: SignUpBody):
    hash_password: str = ""
    stmt = """
    INSERT INTO 
        users(first_name, middle_name, last_name, username, role) VALUES
    VALUES
        (:first_name, :middle_name, :last_name, :username, :role)
    """
    params = {
        "first_name": user.first_name,
        "middle_name": user.middle_name,
        "last_name": user.last_name,
        "username": user.username,
        "role": user.role,
        "password": hash_password,
    }
    try:
        curs.execute(stmt, params)
    except HTTPException:
        raise HTTPException(status_code=401, detail="Failed to create a user")


def update_user(user: UserBase, id: int) -> UserBase:
    stmt = """
        UPDATE users
        SET
            username=:username,
            first_name=:first_name,
            middle_name=:middle_name,
            last_name=:last_name,
        WHERE
            id=:id
    """
    params = {
        "username": user.username,
        "first_name": user.first_name,
        "middle_name": user.middle_name,
        "last_name": user.last_name,
        "id": id,
    }

    curs.execute(stmt, params)
    if curs.rowcount == 0:
        raise HTTPException(status_code=401, detail="Failed to update")
    return user


def update_password(pwd: UserUpdatePassword, username: str):
    user = get_user_or_404(username)
    password = user["password"]

    if checkpw(
        password=pwd.password1,  # type: ignore
        hashed_password=password,
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if pwd.password1 != pwd.password2:
        raise HTTPException(status_code=401, detail="Passwords do not match")

    # decode password
    hash_password = hashpw(password, salt=b"10")

    stmt = """
        UPDATE users
        SET
            password=:hash_password
        WHERE
            username=:username
    """
    params = {"hash_password": hash_password, "username": username}

    curs.execute(stmt, params)
    if curs.rowcount == 0:
        raise HTTPException(status_code=401, detail="Failed to update password")
    return get_user_or_404(username)
