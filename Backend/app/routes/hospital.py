from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.database import Hospital
from app.models.schema import HospitalType, HospitalLoginType
from app.config.config import get_db
from app.functions.password_hash import password_hash, verify_password

router = APIRouter(prefix="/hospital", tags=["hospital"])
# pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

@router.get("/get")
async def get_hospital(hospital_name : str, db: Session = Depends(get_db)):
    result = select(Hospital).where(Hospital.hospital_name == hospital_name)
    result = db.execute(result).scalar_one_or_none()
    if result is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    else:
        return {"found": result.hospital_name}

@router.post("/add")
def add_hospital(hospital: HospitalType, db: Session = Depends(get_db)):
    # hash the password securely
    hashed_password = password_hash(hospital.password)

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



@router.post("/login")
async def login_hospital(hospital_login: HospitalLoginType, db: Session = Depends(get_db)):

    stmt = select(Hospital).where(
        Hospital.hospital_name == hospital_login.hospital_name
    )

    hospital = db.execute(stmt).scalar_one_or_none()

    if hospital is None:
        raise HTTPException(status_code=404, detail="Hospital not found")

    if not verify_password(hospital_login.password, hospital.password_hash):
        raise HTTPException(status_code=401, detail="Invalid password")

    return hospital


@router.delete("/delete")
def delete_hospital(username : str, db: Session = Depends(get_db)):
    stmt = select(Hospital).where(Hospital.hospital_name == username)
    result = db.execute(stmt).scalar_one_or_none()
    if result is None:
        raise HTTPException(status_code=404, detail="Hospital name not found")
    else:
        db.delete(result)
        db.commit()
        return {"deleted": result.hospital_name}