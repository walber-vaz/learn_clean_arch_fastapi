from typing import AsyncGenerator

import pytest_asyncio
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool
from sqlmodel.ext.asyncio.session import AsyncSession

from app.domain import entities
from app.infrastructure.config.database import get_session
from app.infrastructure.config.settings import settings
from app.main import app

TEST_DATABASE_URL = settings.DATABASE_URL.replace(
    'learn_clean_arch_fastapi', 'learn_clean_arch_fastapi_test'
)

test_engine = create_async_engine(
    TEST_DATABASE_URL,
    echo=False,
    future=True,
    poolclass=NullPool,
)

test_async_session = async_sessionmaker(
    test_engine, class_=AsyncSession, expire_on_commit=False
)


@pytest_asyncio.fixture(scope='session')
async def create_tables():
    async with test_engine.begin() as conn:
        await conn.run_sync(entities.SQLModel.metadata.drop_all)
        await conn.run_sync(entities.SQLModel.metadata.create_all)


@pytest_asyncio.fixture
async def db_session(create_tables) -> AsyncGenerator[AsyncSession, None]:
    connection = await test_engine.connect()
    transaction = await connection.begin()
    session = test_async_session(bind=connection)
    try:
        yield session
    finally:
        await session.close()
        await transaction.rollback()
        await connection.close()


@pytest_asyncio.fixture
async def client(db_session) -> AsyncGenerator[TestClient, None]:
    async def override_get_session() -> AsyncGenerator[AsyncSession, None]:
        yield db_session

    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
