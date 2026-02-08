from __future__ import annotations

from collections.abc import Generator
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL = getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@localhost:5432/app",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
