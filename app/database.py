from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings


engine = create_async_engine(settings.DATABASE_URL, echo=True)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession, 
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass 


# Зависимость (Dependency) для FastAPI
# Эта функция будет выдавать сессию для каждого запроса и закрывать её после
async def get_async_session():
    async with async_session_maker() as session:
        yield session