from fastapi import HTTPException, status, Header
from .shemas import User
from . import crud


def get_user_by_token(token: str = Header(..., alias="x-auth-token")) -> User:
    user: User | None = crud.get_user_by_token(token=token)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Auth token invalid!",
    )
