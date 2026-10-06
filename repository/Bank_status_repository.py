from sqlalchemy import select

from repository.Engine import get_session
from models.Bank_status import Bank_Status


async def updete(bank_Status):
    session = get_session()
    result = await session.execute(select(Bank_Status).where(Bank_Status.id == bank_Status.id))
    existing = result.scalar_one_or_none()
    return existing
