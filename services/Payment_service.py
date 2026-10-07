import repository.Payment_repositoiry as rep
import services.Tariff_service as tariff_serv
from models.Payment import Payment

async def add_payment(payment: Payment):
    tariff = await tariff_serv.get_by_id(payment.tariff_id)
    if tariff == None:
        return None
    payment.amount = int(tariff.price)
    if payment.promo_code != None:
        if payment.promo_code.upper() ==  "KVITT010":
            payment.amount = payment.amount * 90 // 100
    return await rep.add(payment)

async def get_payment(id: int):
    return await rep.get(id)