from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.database import Hospital
from app.models.schema import HospitalType
from passlib.context import CryptContext

from app.config.config import get_db

router = APIRouter(prefix="/hospital", tags=["hospital"])
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
@router.post("/add")
def add_hospital(hospital: HospitalType, db: Session = Depends(get_db)):
    # hash the password securely
    salt = "uniproject"
    hashed_password = pwd_context.hash(hospital.password + salt)

    new_hospital = Hospital(
        name=hospital.name,
        email=hospital.email,
        password_hash=hashed_password,
        hospital_name=hospital.hospital_name
    )

    db.add(new_hospital)
    db.commit()
    db.refresh(new_hospital)
    return new_hospital

@router.get("/get")
async def get_hospital(hospital_name : str, db: Session = Depends(get_db)):
    result = select(Hospital).where(Hospital.hospital_name == hospital_name)
    result = db.execute(result).scalar_one_or_none()
    if result is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    else:
        return result

