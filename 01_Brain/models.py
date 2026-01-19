from sqlalchemy import Column, Integer, String, TIMESTAMP, DateTime

from database import Base, engine
from datetime import datetime


class parking_records(Base):
    __tablename__ = "parking_records"

    id = Column(Integer, primary_key=True, index=True)
    car_number = Column(String, nullable = False)
    slot_id = Column(String, nullable = False)
    lift = Column(String)
    entry_time = Column(TIMESTAMP)
    exit_time = Column(TIMESTAMP)
    status = Column(String, nullable = False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)  # ADMIN | SECURITY
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)
