from jose import jwt
from jose.exceptions import JWTError
from config.config import settings
from data import users


from passlib.context import CryptContext

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain: str, hash: str) -> bool:
    return pwd_context.verify(plain, hash)


def get_hash(plain, str) -> str:
    return pwd_context.hash(plain)


def get_jwt_username(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("sub")):
            return None
    except JWTError:
        return None
    return username


def get_current_user(token: str) -> dict | None:
    if not (username := get_jwt_username(token)):
        return None
    if user := lookup_user(username):
        return user
    return None


def lookup_user(username: str) -> dict | None:
    if user := users.get_user_or_404(username):
        return user
    return None


# def auth_user(username: str , plain: str) -> dict | None:
#     if not (user := lookup_user(username)):
#         return None
#     if not verify_password(plain, user.)
