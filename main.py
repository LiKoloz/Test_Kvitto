import os
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import select
from dotenv import load_dotenv

from repository.Engine import AsyncSessionLocal
from models.Tariff import Tariff
from controllers.Tariffs_controllers import router as traffic_router
from controllers.Payment_controller import router as payment_router
from controllers.Bank_status_controller import router as bank_status_router

load_dotenv()


async def seed_tariffs():
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


@asynccontextmanager
async def lifespan(app: FastAPI):
    await seed_tariffs()
    yield


app = FastAPI(
    title="Test Kvitto",
    lifespan=lifespan,
    swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}},
)

app.include_router(traffic_router)
app.include_router(payment_router)
app.include_router(bank_status_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("APP_PORT", "8080")),
    )