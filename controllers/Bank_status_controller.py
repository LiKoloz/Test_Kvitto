import services.Bank_status_service as serv
from fastapi import APIRouter
from models.Bank_status import Bank_Status
from fastapi.responses import JSONResponse
from typing import Any

router = APIRouter(prefix="/webhooks/bank")

@router.post("/")
async def change_bank_status(di: dict[str, Any]):
    bank_status = Bank_Status(**di)
    status = await serv.change_bank_status(bank_status)
    if status == 404:
        return JSONResponse(status_code=status, content={"message": "Не найдено!"})
    return JSONResponse(status_code=status, content={"result": "ok"})