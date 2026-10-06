from models.Base import Base
import os
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession,
)
import asyncio

from sqlalchemy import select
from models.Tariff import Tariff
from models.Base import Base

load_dotenv()
url = os.getenv("DATABASE_URL")  

engine = create_async_engine(url, echo=False)

AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False, autoflush=False,
)

Base.metadata.create_all(bind=engine)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session

async def _seed_tariffs():
    async with AsyncSessionLocal() as session:
        existing = (await session.execute(select(Tariff))).scalars().first()
        if existing:
            return
        session.add_all([
            Tariff(title="basic", price=990000),
            Tariff(title="standard", price=1990000),
            Tariff(title="premium", price=2990000),
        ])
        await session.commit()


asyncio.run(_seed_tariffs())