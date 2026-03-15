from fastapi import APIRouter
from app.models.schema import User
from app.models.database import SessionLocal

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/user/add")
async def add_user(user: User):
    db = SessionLocal()
    new_user = User(
        username = user.username,
        email = user.email,
        first_name = user.first_name,
        last_name = user.last_name,
    )

    db.add(new_user)
    db.commit()
    db.close()
    return user


@router.get("/user")
async def get_user():

    pass