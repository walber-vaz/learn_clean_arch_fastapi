from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.infrastructure.config.database import get_session
from app.infrastructure.repositories.sqlmodel_user_repository import (
    SqlModelUserRepository,
)
from app.use_cases.user.create_user import CreateUserUseCase
from app.use_cases.user.get_user import GetUserUseCase
from app.use_cases.user.list_users import ListUsersUseCase


def get_user_repository(
    session: AsyncSession = Depends(get_session),
) -> SqlModelUserRepository:
    return SqlModelUserRepository(session)  # pragma: no cover


def get_create_user_use_case(
    user_repository: SqlModelUserRepository = Depends(get_user_repository),
) -> CreateUserUseCase:
    return CreateUserUseCase(user_repository)  # pragma: no cover


def get_get_user_use_case(
    user_repository: SqlModelUserRepository = Depends(get_user_repository),
) -> GetUserUseCase:
    return GetUserUseCase(user_repository)  # pragma: no cover


def get_list_users_use_case(
    user_repository: SqlModelUserRepository = Depends(get_user_repository),
) -> ListUsersUseCase:
    return ListUsersUseCase(user_repository)  # pragma: no cover
