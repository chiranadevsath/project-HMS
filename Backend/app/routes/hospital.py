from fastapi import APIRouter

from app.models.schema import Hospital
from app.models.database import SessionLocal

APIRouter = APIRouter(prefix="/hospital", tags=["hospital"])

@router.post("/hospital/add")
async def add_hospital(hospital : Hospital):
    db = SessionLocal()
    new_user = Hospital(
        user = hospital.username,
        email=hospital.email,
        name=hospital.name,

    )

    db.add(new_user)
    db.commit()
    db.close()
    pass