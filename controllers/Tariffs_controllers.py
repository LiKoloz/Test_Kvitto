from fastapi import APIRouter
import services.Tarrif_service as serv
from fastapi.encoders import jsonable_encoder

from fastapi.responses import JSONResponse

router = APIRouter(prefix="/tariffs")

@router.get("/")
async def get_all_tariffs():
    res =  await serv.get_all_tariffs()
    return jsonable_encoder(res) 