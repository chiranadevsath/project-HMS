from pydantic import BaseModel

class Hospital(BaseModel):
    hospital_id: int
    name: str
    email: str

    class Config:
        title = "Hospital"
        from_attributes = True

class User(BaseModel):
    username : str
    first_name : str
    last_name : str
    email : str
    hospital_id : int

    class Config:
        title = "User"
        from_attributes = True