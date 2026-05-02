from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_conf import get_db
from crud import composers

router = APIRouter(prefix="/api/composers", tags=["composers"])

@router.get("")
async def get_composers(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    composers_list = await composers.get_composers(db, skip, limit)

    return {
        "code": 200,
        "msg":"successfully get composers",
        "data": composers_list
    }

@router.get("/works")
async def get_works(
        composer_id: int = Query(..., alias= "composerId"),
        page: int = 1,
        page_size: int = Query(2, alias="pageSize"),
        db: AsyncSession = Depends(get_db)
):
    offset = (page - 1) * page_size
    works = await composers.get_works(db, composer_id, offset, page_size)
    total = await composers.get_works_count(db, composer_id)

    has_more: bool = total > (offset + len(works))

    return {
        "code": 200,
        "msg": "successfully get composer",
        "data": {
            "composerId": composer_id,
            "works" : works,
            "total" : total,
            "hasMore" : has_more,
        }
    }