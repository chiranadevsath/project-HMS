from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.models.database import Base, engine

from app.routes import data, user , hospital


app = FastAPI()

# Tell the fastapi backend where the files to the routers are to direct the data
app.include_router(data.router)
app.include_router(user.router)
app.include_router(hospital.router)

origins = [
    "http://localhost",
    "http://localhost:3000/*",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000/*",
    "http://127.0.0.1:8000/*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


# connect to the database




@app.get("/")
def read_root():
    return {"Hello": "This is the backend of Hospital Management System 🏥"}




