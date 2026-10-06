from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from repository.Engine import get_session
from models.Tariff import Tariff


async def get_all_tariffs():
    session = get_session()

    result = await session.execute(select(Tariff))
    return result.scalars().all()