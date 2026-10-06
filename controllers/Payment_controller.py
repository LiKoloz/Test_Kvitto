from fastapi import APIRouter
import services.Payment_service as serv
import json
from models.Payment import Payment
from fastapi import Header
from fastapi.responses import JSONResponse

router = APIRouter(prefix="payments")

@router.get("/{id}")
async def get_by_id(id:int):
    a = await serv.get_payment(id)
    if a:
        res = json.dumps(a)
        return JSONResponse(content=res)
    return JSONResponse(
                status_code=404, 
                content={ "message": "Платеж не найден" }
        )

@router.post("/")
async def add_payment(
    payment: Payment,
    idempotency_key: str | None = Header(default=None, alias="Idempotency-Key")
    ):
    if idempotency_key == None:
        res = await serv.add_payment(payment)
        if res:
            return JSONResponse(status_code=201, content={"message": "Платеж создан"})
        return JSONResponse(status_code=500, content={"message": "Ошибка сервера, платеж не создан"})
    else:
        a = await serv.get_payment(id)
        if a:
            res = json.dumps(a)
            return JSONResponse(content=res)
        return JSONResponse(
                    status_code=404, 
                    content={ "message": "Платеж не найден" }
                )