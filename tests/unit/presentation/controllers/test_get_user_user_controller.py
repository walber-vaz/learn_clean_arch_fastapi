from datetime import datetime
from http import HTTPStatus
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest
from fastapi import HTTPException

from app.domain.entities.user import User
from app.presentation.controllers.user_controller import get_user
from app.presentation.schemas.user.response import UserResponse
from app.use_cases.user.get_user import GetUserInput, GetUserOutput
from tests.mocks.user import User as MockUser

user_mock = MockUser()


@pytest.mark.asyncio
async def test_get_user_success():
    now = datetime.now()

    user_id = user_mock.id

    user = User(
        id=user_id,
        name=user_mock.name,
        email=user_mock.email,
        password=user_mock.password,
        created_at=now,
    )

    mock_use_case = AsyncMock()
    mock_use_case.execute.return_value = GetUserOutput(user=user)

    response = await get_user(
        user_id=user_id,
        use_case=mock_use_case,
    )

    assert response == UserResponse(
        id=user_id,
        name=user_mock.name,
        email=user_mock.email,
        created_at=now,
    )
    assert response.id == user_id
    assert response.name == user_mock.name
    assert response.email == user_mock.email
    assert response.created_at == now

    mock_use_case.execute.assert_called_once_with(
        input_data=GetUserInput(user_id=user_id)
    )


@pytest.mark.asyncio
async def test_get_user_not_found():
    user_id = uuid4()

    mock_use_case = AsyncMock()
    mock_use_case.execute.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        await get_user(
            user_id=user_id,
            use_case=mock_use_case,
        )

    assert exc_info.value.status_code == HTTPStatus.NOT_FOUND

    mock_use_case.execute.assert_called_once_with(
        input_data=GetUserInput(user_id=user_id)
    )
