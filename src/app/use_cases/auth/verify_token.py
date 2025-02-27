from dataclasses import dataclass
from typing import Optional

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.security.jwt import TokenPayload, decode_access_token
from app.use_cases.interfaces.use_case import UseCase


@dataclass
class VerifyTokenInput:
    token: str


@dataclass
class VerifyTokenOutput:
    user: Optional[User] = None
    is_valid: bool = False


class VerifyTokenUseCase(UseCase[VerifyTokenInput, VerifyTokenOutput]):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, input_data: VerifyTokenInput) -> VerifyTokenOutput:
        try:
            payload: TokenPayload | ValueError = decode_access_token(
                input_data.token
            )
            user_id = payload.sub
            if not user_id:
                return VerifyTokenOutput(is_valid=False)

            user = await self.user_repository.find_by_id(user_id)
            if not user:
                return VerifyTokenOutput(is_valid=False)

            return VerifyTokenOutput(user=user, is_valid=True)
        except ValueError:
            return VerifyTokenOutput(is_valid=False)
