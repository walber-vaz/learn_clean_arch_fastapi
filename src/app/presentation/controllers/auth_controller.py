from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.config.settings import settings
from app.infrastructure.dependencies.user_dependencies import (
    get_user_repository,
)
from app.presentation.schemas.auth.response import TokenResponse
from app.use_cases.auth.login_user import LoginUserInput, LoginUserUseCase

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_PREFIX}/auth/login'
)


@router.post('/login', response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_repository: UserRepository = Depends(get_user_repository),
):
    use_case = LoginUserUseCase(user_repository)
    input_data = LoginUserInput(
        email=form_data.username,
        password=form_data.password,
    )

    result = await use_case.execute(input_data)

    if not result.success or not result.access_token:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Email ou senha incorretos',
            headers={'WWW-Authenticate': 'Bearer'},
        )

    return TokenResponse(access_token=result.access_token)
