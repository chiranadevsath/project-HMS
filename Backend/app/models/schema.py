from pydantic import BaseModel

class HospitalType(BaseModel):
    name: str
    email: str
    password : str
    hospital_name : str


class User(BaseModel):
    username : str
    first_name : str
    last_name : str
    email : str
    hospital_id : int

    class Config:
        from_attributes = True