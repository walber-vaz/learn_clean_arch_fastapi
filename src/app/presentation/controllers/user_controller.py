from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.infrastructure.dependencies.user_dependencies import (
    get_create_user_use_case,
    get_get_user_use_case,
    get_list_users_use_case,
)
from app.presentation.schemas.user.request import UserCreateRequest
from app.presentation.schemas.user.response import UserResponse
from app.use_cases.user.create_user import CreateUserUseCase
from app.use_cases.user.get_user import GetUserInput, GetUserUseCase
from app.use_cases.user.list_users import ListUsersUseCase

router = APIRouter()


@router.post('/users', response_model=UserResponse)
async def create_user(
    user_request: UserCreateRequest,
    use_case: CreateUserUseCase = Depends(get_create_user_use_case),
):
    try:
        data = await use_case.execute(input_data=user_request)

        return UserResponse(
            id=data.user.id,
            name=data.user.name,
            email=data.user.email,
            created_at=data.user.created_at,
        )
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))


@router.get('/users/{user_id}', response_model=UserResponse)
async def get_user(
    user_id: UUID, use_case: GetUserUseCase = Depends(get_get_user_use_case)
):
    data = await use_case.execute(input_data=GetUserInput(user_id=user_id))

    if data is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    return UserResponse(
        id=data.user.id,
        name=data.user.name,
        email=data.user.email,
        created_at=data.user.created_at,
    )


@router.get('/users', response_model=list[UserResponse])
async def list_users(
    use_case: ListUsersUseCase = Depends(get_list_users_use_case),
):
    data = await use_case.execute()

    return [
        UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            created_at=user.created_at,
        )
        for user in data.users
    ]
