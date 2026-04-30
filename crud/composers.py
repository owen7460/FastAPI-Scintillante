from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.composers import Composers


async def get_composers(db:AsyncSession, skip: int = 0, limit: int = 100):
    stmt = select(Composers).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()