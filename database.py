import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

IS_VERCEL = os.getenv("VERCEL") == "1"

if IS_VERCEL:
    DATABASE_URL = "sqlite:///:memory:"  # DB en memoria (no persistente)
else:
    DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
