from dataclasses import dataclass
from typing import Optional

from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.security.jwt import create_access_token
from app.infrastructure.security.password import verify_password
from app.use_cases.interfaces.use_case import UseCase


@dataclass
class LoginUserInput:
    email: str
    password: str


@dataclass
class LoginUserOutput:
    access_token: Optional[str] = None
    success: bool = False


class LoginUserUseCase(UseCase[LoginUserInput, LoginUserOutput]):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, input_data: LoginUserInput) -> LoginUserOutput:
        user = await self.user_repository.find_by_email(input_data.email)

        if not user:
            return LoginUserOutput(success=False)

        if not verify_password(input_data.password, user.hashed_password):
            return LoginUserOutput(success=False)

        access_token = create_access_token(subject=str(user.id))
        return LoginUserOutput(access_token=access_token, success=True)
