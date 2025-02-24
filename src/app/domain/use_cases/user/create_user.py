from dataclasses import dataclass
from http import HTTPStatus

from fastapi import HTTPException

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.domain.use_cases.interfaces.use_case import UseCase


@dataclass
class CreateUserInput:
    name: str
    email: str
    password: str


@dataclass
class CreateUserOutput:
    user: User


class CreateUserUseCase(UseCase[CreateUserInput, CreateUserOutput]):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, input_data: CreateUserInput) -> CreateUserOutput:
        existing_user = await self.user_repository.find_by_email(input_data.email)
        if existing_user:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="User already exists"
            )

        user = User(
            name=input_data.name, email=input_data.email, password=input_data.password
        )

        created_user = await self.user_repository.create(user)

        return CreateUserOutput(user=created_user)
