from fastapi import APIRouter

from users import crud
from users.schemas import CreateUser

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
