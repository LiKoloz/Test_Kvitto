import repository.Bank_status_repository as rep

async def change_bank_status(status):
    a = await rep.updete(status)
    if a == None:
        return 404
    return 200