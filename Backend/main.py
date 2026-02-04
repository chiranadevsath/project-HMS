from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.models.database import Base, engine

from app.routes import data

app = FastAPI()
app.include_router(data.router)

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

@app.get("/")
def read_root():
    return {"Hello": "This is the backend of Hospital Management System 🏥"}




