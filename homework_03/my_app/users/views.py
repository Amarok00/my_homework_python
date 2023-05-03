from fastapi import APIRouter, HTTPException, status, Depends
from .shemas import UserOut, UserIn, User
from . import crud
from .dependensins import get_user_by_token

router = APIRouter(
    tags=["Users"],
)


@router.get("/", response_model=list[UserOut])
def get_users() -> list:
    return crud.get_users()


@router.post("/", response_model=UserOut, description="Create a new user")
def create_user(user_in: UserIn):
    return crud.create_user(user_in=user_in)


@router.get("/me/", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_token)):
    return User


@router.get(
    "/{user_id}/",
    response_model=UserOut,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": UserOut, "description": "User not found"}
    },
)
def get_user_by_id(user_id: int) -> User:
    user: User | None = crud.get_user_by_id(user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )
    return user
