import repository.Tariff_repository as rep

async def get_all_tariffs():
    return await rep.get()

async def get_by_id(id : int):
    return await rep.get_by_id(id)