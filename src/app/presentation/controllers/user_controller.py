from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query

from app.infrastructure.dependencies.auth_dependencies import get_current_user
from app.infrastructure.dependencies.user_dependencies import (
    get_create_user_use_case,
    get_get_user_use_case,
    get_list_users_use_case,
)
from app.presentation.schemas.common.pagination import PaginatedResponse
from app.presentation.schemas.user.request import UserCreateRequest
from app.presentation.schemas.user.response import UserResponse
from app.use_cases.user.create_user import CreateUserUseCase
from app.use_cases.user.get_user import GetUserInput, GetUserUseCase
from app.use_cases.user.list_users import ListUsersInput, ListUsersUseCase

router = APIRouter()


@router.post('/', response_model=UserResponse, status_code=HTTPStatus.CREATED)
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


@router.get(
    '/{user_id}/',
    response_model=UserResponse,
    dependencies=[Depends(get_current_user)],
)
async def get_user(
    user_id: UUID,
    use_case: GetUserUseCase = Depends(get_get_user_use_case),
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


@router.get(
    '/',
    response_model=PaginatedResponse[UserResponse],
    dependencies=[Depends(get_current_user)],
)
async def list_users(
    page: int = Query(1, ge=1, description='Page number'),
    page_size: int = Query(10, ge=1, le=100, description='Page size'),
    use_case: ListUsersUseCase = Depends(get_list_users_use_case),
):
    data = await use_case.execute(
        input_data=ListUsersInput(
            page=page,
            page_size=page_size,
        )
    )

    users_list = [
        UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            created_at=user.created_at,
        )
        for user in data.users
    ]

    pagination = PaginatedResponse(
        page=page,
        page_size=page_size,
        items=users_list,
        total=data.total,
        total_pages=data.total_pages,
    )

    return pagination
