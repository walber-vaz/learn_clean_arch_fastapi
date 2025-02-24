from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.use_cases.interfaces.use_case import UseCase


@dataclass
class GetUserInput:
    user_id: UUID


@dataclass
class GetUserOutput:
    user: Optional[User]


class GetUserUseCase(UseCase[GetUserInput, GetUserOutput]):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, input_data: GetUserInput) -> GetUserOutput:
        user = await self.user_repository.find_by_id(input_data.user_id)

        return GetUserOutput(user=user)
