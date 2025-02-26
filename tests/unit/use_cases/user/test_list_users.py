from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from app.domain.entities.user import User
from app.use_cases.user.list_users import ListUsersInput, ListUsersUseCase
from tests.mocks.user import User as MockUser

user_mock = MockUser()


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_list_users_use_case_success():
    mock_repo = AsyncMock()

    mock_users = [
        User(
            id=uuid4(),
            name=f'{user_mock.name} {i}',
            email=f'{user_mock.email.split("@")[0]}+{i}@{
                user_mock.email.split("@")[1]
            }',
            password=user_mock.password,
        )
        for i in range(15)
    ]

    mock_repo.index.return_value = mock_users

    page = 2
    page_size = 10

    use_case = ListUsersUseCase(mock_repo)
    input_data = ListUsersInput(page=page, page_size=page_size)

    result = await use_case.execute(input_data)

    assert result.users == mock_users
    assert result.total == len(mock_users)
    assert result.total_pages == page

    mock_repo.index.assert_called_once_with(page, page_size)


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_list_users_use_case_empty_result():
    mock_repo = AsyncMock()

    mock_repo.index.return_value = []

    page = 1
    page_size = 10

    use_case = ListUsersUseCase(mock_repo)
    input_data = ListUsersInput(page=page, page_size=page_size)

    result = await use_case.execute(input_data)

    assert result.users == []
    assert result.total == 0
    assert result.total_pages == 0

    mock_repo.index.assert_called_once_with(page, page_size)


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_list_users_use_case_exact_page_size():
    mock_repo = AsyncMock()

    page_size = 10
    mock_users = [
        User(
            id=uuid4(),
            name=f'{user_mock.name} {i}',
            email=f'{user_mock.email.split("@")[0]}+{i}@{
                user_mock.email.split("@")[1]
            }',
            password=user_mock.password,
        )
        for i in range(page_size)
    ]

    mock_repo.index.return_value = mock_users

    page = 1

    use_case = ListUsersUseCase(mock_repo)
    input_data = ListUsersInput(page=page, page_size=page_size)

    result = await use_case.execute(input_data)

    assert result.users == mock_users
    assert result.total == len(mock_users)
    assert result.total_pages == page

    mock_repo.index.assert_called_once_with(page, page_size)
