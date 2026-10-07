from sqlalchemy import select

from repository.Engine import get_session
from models.Bank_status import Bank_Status
from repository.Engine import AsyncSessionLocal

async def updete(bank_Status):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Bank_Status).where(Bank_Status.id == bank_Status.id))
        existing = result.scalar_one_or_none()
        return existing
