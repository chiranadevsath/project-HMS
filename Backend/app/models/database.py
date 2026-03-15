from dotenv import load_dotenv
import os
from sqlalchemy import Integer, create_engine, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql.schema import Column, ForeignKey

load_dotenv()


# Load the .env for security instead of the direct link and use dotenv to bring the environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Error Check
if not DATABASE_URL:
    raise ValueError("DATABASE_URL must be set in .env file.")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True , autoincrement=True)
    username = Column(String, nullable = False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    hospital_id = Column(Integer, ForeignKey("hospital.id"))
    email = Column(String, nullable = False)



class Hospital(Base):
    __tablename__ = "hospital"
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String, nullable = False)
    hospital_name = Column(String, nullable = False)
    address = Column(String, nullable = False)


class UserPosition(Base):
    __tablename__ = "user_position"
    id = Column(Integer, primary_key = True, autoincrement=True)
    hospital_id = Column(Integer, ForeignKey("hospital.id"))
    user_name = Column(String, nullable = False)
    position = Column(String, nullable = False)

class UserAuthorization(Base):
    __tablename__ = "authorization"
    id = Column(Integer, primary_key = True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    password_hash = Column(String, nullable = False)

class HospitalAuthorization(Base):
    __tablename__ = "hospital_authorization"
    id = Column(Integer, primary_key = True , autoincrement=True)
    hospital_id = Column(Integer, ForeignKey("hospital.id"))
    password_hash = Column(String, nullable = False)


