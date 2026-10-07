import repository.Payment_repositoiry as rep
import services.Tarrif_service as tariff_serv
from models.Payment import Payment

async def add_payment(payment: Payment):
    tariff = await tariff_serv.get_by_id(payment.tarrif_id)
    payment.amount = tariff.price * 100
    if payment.promo_code.upper() ==  "KVITT010":
        payment.amount *= 90 // 100
    return await rep.add(payment)

async def get_payment(id):
    return await rep.get(id)