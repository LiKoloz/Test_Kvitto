from sqlalchemy import select

from repository.Engine import get_session
from models.Payment import Payment
from repository.Engine import AsyncSessionLocal

async def add(payment: Payment):
     async with AsyncSessionLocal() as session:
        try:
            session.add(payment)
            await session.commit()
            await session.refresh(payment)
        except:
            return False
        return True

async def get(id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Payment).where(Payment.id == id))
        return result.scalar_one_or_none()