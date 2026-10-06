import repository.Payment_repositoiry as rep

async def add_payment(payment):
    return await rep.add(payment)

async def get_payment(id):
    return await rep.get(id)