import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", default="sqlite:///::memory:"
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_local = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()


async def get_db():
    async with async_session_local() as db:
        try:
            yield db
        finally:
            await db.close()
