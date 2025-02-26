from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from app.domain.entities.user import User
from app.use_cases.user.get_user import GetUserInput, GetUserUseCase
from tests.mocks.user import User as MockUser


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_get_user_use_case_success():
    mock_repo = AsyncMock()

    user_mock = MockUser()
    mock_user = User(
        id=user_mock.id,
        name=user_mock.name,
        email=user_mock.email,
        password=user_mock.password,
    )

    mock_repo.find_by_id.return_value = mock_user

    use_case = GetUserUseCase(mock_repo)

    input_data = GetUserInput(user_id=user_mock.id)

    result = await use_case.execute(input_data)

    assert result.user is not None
    assert result.user.id == user_mock.id
    assert result.user.name == user_mock.name
    assert result.user.email == user_mock.email
    assert result.user.password == user_mock.password

    mock_repo.find_by_id.assert_called_once_with(user_mock.id)


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_user_use_case_user_not_found():
    mock_repo = AsyncMock()

    mock_repo.find_by_id.return_value = None

    use_case = GetUserUseCase(mock_repo)

    user_id = uuid4()

    input_data = GetUserInput(user_id=user_id)

    result = await use_case.execute(input_data)

    assert result.user is None

    mock_repo.find_by_id.assert_called_once_with(user_id)
