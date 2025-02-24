from dataclasses import dataclass

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.use_cases.interfaces.use_case import UseCase


@dataclass
class ListUsersInput:
    pass


@dataclass
class ListUsersOutput:
    users: list[User]


class ListUsersUseCase(UseCase[ListUsersInput, ListUsersOutput]):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(
        self, input_data: ListUsersInput = None
    ) -> ListUsersOutput:
        users = await self.user_repository.index()

        return ListUsersOutput(users=users)
