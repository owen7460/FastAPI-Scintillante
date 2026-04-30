from fastapi import APIRouter

router = APIRouter(prefix="/api/composers", tags=["composers"])

@router.get("/categories")
async def get_categories(skip: int = 0, limit: int = 100):
    return {
        "code": 200,
        "msg":"successfully get categories",
        "data": "composer list"
    }