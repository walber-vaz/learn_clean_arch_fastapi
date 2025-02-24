from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from app.infrastructure.config.settings import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)


async def get_session() -> AsyncIterator[AsyncSession]:
    async_session = async_sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
