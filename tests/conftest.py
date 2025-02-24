import asyncio
from typing import AsyncGenerator

import pytest_asyncio
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

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
    connect_args={'check_same_thread': False},
)

test_async_session = sessionmaker(
    test_engine, class_=AsyncSession, expire_on_commit=False
)


@pytest_asyncio.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='function')
async def setup_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(
            entities.SQLModel.metadata.create_all, bind=test_engine
        )

    yield

    async with test_engine.begin() as conn:
        await conn.run_sync(
            entities.SQLModel.metadata.drop_all, bind=test_engine
        )

    await test_engine.dispose()


@pytest_asyncio.fixture(scope='function')
async def session(
    setup_database,
) -> AsyncGenerator[AsyncSession, None]:
    async with test_async_session() as session:
        try:
            yield session
        finally:
            await session.rollback()
            await session.close()


@pytest_asyncio.fixture(scope='function')
async def client(session):
    async def override_get_session():
        try:
            yield session
        finally:
            pass

    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
