from fastapi import APIRouter
from users.schemas import CreateUser


router = APIRouter(prefix="/users")

@router.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }