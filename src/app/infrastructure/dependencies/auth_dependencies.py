from http import HTTPStatus

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.config.settings import settings
from app.infrastructure.dependencies.user_dependencies import (
    get_user_repository,
)
from app.use_cases.auth.verify_token import (
    VerifyTokenInput,
    VerifyTokenUseCase,
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_PREFIX}/auth/login'
)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_repository: UserRepository = Depends(get_user_repository),
) -> User:
    use_case = VerifyTokenUseCase(user_repository)
    result = await use_case.execute(VerifyTokenInput(token=token))

    if not result.is_valid or not result.user:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Token inválido ou expirado',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    return result.user
