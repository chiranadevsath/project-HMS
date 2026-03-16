from dotenv import load_dotenv
import os
from sqlalchemy import Integer, create_engine, String
from sqlalchemy.orm import sessionmaker, declarative_base


load_dotenv()


# Load the .env for security instead of the direct link and use dotenv to bring the environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Error Check
if not DATABASE_URL:
    raise ValueError("DATABASE_URL must be set in .env file.")

engine = create_engine(DATABASE_URL, echo= True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(engine)

def close_db():
    Base.metadata.drop_all(engine)