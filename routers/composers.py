from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_conf import get_db
from crud import composers

router = APIRouter(prefix="/api/composers", tags=["composers"])

@router.get("/categories")
async def get_categories(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    composers_list = await composers.get_composers(db ,skip,limit)

    return {
        "code": 200,
        "msg":"successfully get composers",
        "data": composers_list
    }