from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from models.composers import Composers, Works


async def get_composers(db:AsyncSession, skip: int = 0, limit: int = 100):
    stmt = select(Composers).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

async def get_works(db:AsyncSession, composer_id: int, skip: int = 0, limit: int = 2):
    stmt = select(Works).where(Works.composer_id == composer_id).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

async def get_works_count(db:AsyncSession, composer_id: int):
    stmt = select(func.count(Works.id)).where(Works.composer_id == composer_id)
    result = await db.execute(stmt)
    return result.scalar_one()