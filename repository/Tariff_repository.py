from sqlalchemy import select
import traceback
from repository.Engine import AsyncSessionLocal
from models.Tariff import Tariff


async def get():
    async with AsyncSessionLocal() as session:
        try:
            result = await session.execute(select(Tariff))
            return result.scalars().all()
        except Exception as e:
            print(">>> REAL ERROR:", repr(e))
            traceback.print_exc()
            raise

async def get_by_id(id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Tariff).where(Tariff.id == id))
        return result.scalar_one_or_none()