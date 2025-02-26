from datetime import datetime
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from app.domain.entities.user import User
from app.presentation.controllers.user_controller import list_users
from app.presentation.schemas.common.pagination import PaginatedResponse
from app.presentation.schemas.user.response import UserResponse
from app.use_cases.user.list_users import ListUsersInput, ListUsersOutput
from tests.mocks.user import User as MockUser

user_mock = MockUser()


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_list_users_endpoint():
    now = datetime.now()

    page = 2
    page_size = 15
    total = 40
    total_pages = 3

    mock_users = [
        User(
            id=uuid4(),
            name=f'{user_mock.name} {i}',
            email=f'{user_mock.email.split("@")[0]}+{i}@{
                user_mock.email.split("@")[1]
            }',
            password=user_mock.password,
            created_at=now,
        )
        for i in range(3)
    ]

    mock_use_case = AsyncMock()
    mock_use_case.execute.return_value = ListUsersOutput(
        users=mock_users,
        total=total,
        total_pages=total_pages,
    )

    response = await list_users(
        page=page,
        page_size=page_size,
        use_case=mock_use_case,
    )

    assert isinstance(response, PaginatedResponse)

    assert response.page == page
    assert response.page_size == page_size
    assert response.total == total
    assert response.total_pages == total_pages

    assert len(response.items) == len(mock_users)
    for i, item in enumerate(response.items):
        assert isinstance(item, UserResponse)
        assert item.id == mock_users[i].id
        assert item.name == mock_users[i].name
        assert item.email == mock_users[i].email
        assert item.created_at == mock_users[i].created_at

    mock_use_case.execute.assert_called_once_with(
        input_data=ListUsersInput(
            page=page,
            page_size=page_size,
        )
    )


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_list_users_empty():
    page = 1
    page_size = 10

    mock_use_case = AsyncMock()
    mock_use_case.execute.return_value = ListUsersOutput(
        users=[],
        total=0,
        total_pages=0,
    )

    response = await list_users(
        page=page,
        page_size=page_size,
        use_case=mock_use_case,
    )

    assert isinstance(response, PaginatedResponse)

    assert response.page == page
    assert response.page_size == page_size
    assert response.total == 0
    assert response.total_pages == 0

    assert len(response.items) == 0

    mock_use_case.execute.assert_called_once_with(
        input_data=ListUsersInput(
            page=page,
            page_size=page_size,
        )
    )
