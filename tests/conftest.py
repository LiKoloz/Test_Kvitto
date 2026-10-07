import os

# ВАЖНО: до импорта main/Engine
os.environ["DATABASE_URL"] = "postgresql+asyncpg://postgres:123@postgres:5432/Kvitto_test"

import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from repository.Engine import engine, AsyncSessionLocal
from models.Base import Base
from models.Tariff import Tariff
from main import app


@pytest_asyncio.fixture(autouse=True)
async def prepare_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as s:
        s.add_all([
            Tariff(id=1, title="basic",    price=990000),
            Tariff(id=2, title="standard", price=1990000),
            Tariff(id=3, title="premium",  price=2990000),
        ])
        await s.commit()
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        yield ac