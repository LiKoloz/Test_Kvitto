import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession,
)

load_dotenv()
url = os.getenv("DATABASE_URL")

engine = create_async_engine(url, echo=False)

AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False, autoflush=False,
)


async def get_session():
    async with AsyncSessionLocal() as session:
        yield session