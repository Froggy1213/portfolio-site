from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Project

async def get_active_projects(session: AsyncSession) -> list[Project]:
    stmt = select(Project).where(Project.is_active == True).order_by(Project.order.desc())
    result = await session.execute(stmt)
    return list(result.scalars().all())