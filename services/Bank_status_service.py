import repository.Bank_status_repository as rep
from models.Bank_status import Bank_Status

async def change_bank_status(status: Bank_Status):
    a = await rep.updete(status)
    if a == None:
        return 404
    return 200