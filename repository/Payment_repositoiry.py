from sqlalchemy import select

from repository.Engine import get_session
from models.Payment import Payment


async def add_payment(payment):
    session = get_session()
    try:
        session.add(payment)
        await session.commit()
        await session.refresh(payment)
    except:
        return False
    return True

async def get_all_payment(id):
    session = get_session()
    result = await session.execute(select(Payment).where(Payment.id == id))
    return result.scalar_one_or_none()