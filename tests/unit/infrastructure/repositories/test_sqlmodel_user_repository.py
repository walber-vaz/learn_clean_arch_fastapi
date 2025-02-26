import pytest

from app.domain.entities.user import User
from app.infrastructure.repositories.sqlmodel_user_repository import (
    SqlModelUserRepository,
)
from tests.mocks.user import User as UserMock

user_mock = UserMock()


@pytest.mark.asyncio
async def test_create_user(db_session):
    repository = SqlModelUserRepository(db_session)
    user = User(
        email=user_mock.email,
        password=user_mock.password,
        name=user_mock.name,
        id=user_mock.id,
    )

    created_user = await repository.create(user)

    assert created_user.id == user.id
    assert created_user.email == user.email
    assert created_user.name == user.name

    found_user = await repository.find_by_id(user.id)

    assert found_user is not None
    assert found_user.id == user.id
    assert found_user.email == user.email
    assert found_user.name == user.name
