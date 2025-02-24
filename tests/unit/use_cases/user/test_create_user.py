from unittest.mock import AsyncMock

import pytest
from fastapi import HTTPException

from app.domain.entities.user import User
from app.infrastructure.security.password import get_password_hash
from app.use_cases.user.create_user import CreateUserUseCase
from tests.mocks.user import User as MockUser


async def test_create_user_use_case_success():
    mock_repo = AsyncMock()
    mock_repo.find_by_email.return_value = None

    user_mock = MockUser()

    created_user = User(
        id=user_mock.id,
        name=user_mock.name,
        email=user_mock.email,
        password=get_password_hash(user_mock.password),
    )
    mock_repo.create.return_value = created_user

    use_case = CreateUserUseCase(mock_repo)

    result = await use_case.execute(user_mock)

    assert result.user.id == user_mock.id
    assert result.user.name == user_mock.name
    assert result.user.email == user_mock.email

    mock_repo.find_by_email.assert_called_once_with(user_mock.email)
    mock_repo.create.assert_called_once()


async def test_create_user_use_case_email_already_exists():
    mock_repo = AsyncMock()
    mock_repo.find_by_email.return_value = User()

    use_case = CreateUserUseCase(mock_repo)

    with pytest.raises(HTTPException, match='User already exists'):
        await use_case.execute(MockUser())

    mock_repo.find_by_email.assert_called_once_with(MockUser().email)
