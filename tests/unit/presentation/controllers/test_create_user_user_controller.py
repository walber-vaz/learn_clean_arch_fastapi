from datetime import datetime
from http import HTTPStatus
from unittest.mock import AsyncMock

import pytest
from fastapi import HTTPException

from app.domain.entities.user import User
from app.presentation.controllers.user_controller import create_user
from app.presentation.schemas.user.request import UserCreateRequest
from app.presentation.schemas.user.response import UserResponse
from app.use_cases.user.create_user import CreateUserOutput
from tests.mocks.user import User as MockUser

user_mock = MockUser()


@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_user_endpoint():
    now = datetime.now()

    user = User(
        id=user_mock.id,
        name=user_mock.name,
        email=user_mock.email,
        password=user_mock.password,
        created_at=now,
    )

    request = UserCreateRequest(
        name=user_mock.name,
        email=user_mock.email,
        password=user_mock.password,
    )

    mock_use_case = AsyncMock()
    mock_use_case.execute.return_value = CreateUserOutput(user=user)

    response = await create_user(
        request,
        use_case=mock_use_case,
    )

    assert response == UserResponse(
        id=user_mock.id,
        name=user_mock.name,
        email=user_mock.email,
        created_at=now,
    )
    assert response.id == user_mock.id
    assert response.name == user_mock.name
    assert response.email == user_mock.email
    assert response.created_at == now

    mock_use_case.execute.assert_called_once_with(input_data=request)


@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_create_user_endpoint_value_error():
    request = UserCreateRequest(
        name=user_mock.name,
        email=user_mock.email,
        password=user_mock.password,
    )

    mock_use_case = AsyncMock()
    error_message = 'Email inválido'
    mock_use_case.execute.side_effect = ValueError(error_message)

    with pytest.raises(HTTPException) as exc_info:
        await create_user(
            request,
            use_case=mock_use_case,
        )

    assert exc_info.value.status_code == HTTPStatus.BAD_REQUEST
    assert exc_info.value.detail == error_message

    mock_use_case.execute.assert_called_once_with(input_data=request)
