import repository.Tariff_repository as rep

async def get_all_tariffs():
    return await rep.get()