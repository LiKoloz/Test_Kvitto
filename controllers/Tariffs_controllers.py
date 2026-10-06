from fastapi import APIRouter
import services.Tarrif_service as serv
import json

from fastapi.responses import JSONResponse

router = APIRouter(prefix="tariffs")

@router.get("/")
async def get_all_tariffs():
    res =  serv.get_all_tariffs()
    res_js = json.dumps(res)
    return JSONResponse(content=res_js)