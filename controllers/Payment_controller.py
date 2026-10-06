from fastapi import APIRouter
import services.Payment_service as serv
import json
from models.Payment import Payment
from fastapi import Header
from fastapi.responses import JSONResponse
from typing import Any
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/payments")

@router.get("/{id}")
async def get_by_id(id:int):
    res = await serv.get_payment(id)
    if res:
        return jsonable_encoder(res)
    return JSONResponse(
                status_code=404, 
                content={ "message": "Платеж не найден" }
        )

@router.post("/")
async def add_payment(
    di: dict[str, Any],
    idempotency_key: str | None = Header(default=None, alias="Idempotency-Key"),
):
    payment = Payment(**di)
    if idempotency_key == None:
        res = await serv.add_payment(payment)
        if res:
            return JSONResponse(status_code=201, content={"message": "Платеж создан"})
        return JSONResponse(status_code=500, content={"message": "Ошибка сервера, платеж не создан"})
    else:
        payment.id = int(idempotency_key)
        res = await serv.get_payment(payment.id)
        if res:
            return jsonable_encoder(res)
        return JSONResponse(
                    status_code=404, 
                    content={ "message": "Платеж не найден" }
                )