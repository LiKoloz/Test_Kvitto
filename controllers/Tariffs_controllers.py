from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

@router.get("/")
async def get_all_tariffs():
    return