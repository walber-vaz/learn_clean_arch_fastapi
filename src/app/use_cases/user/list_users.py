from dataclasses import dataclass

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.use_cases.interfaces.use_case import UseCase


@dataclass
class ListUsersInput:
    page: int
    page_size: int


@dataclass
class ListUsersOutput:
    users: list[User]
    total: int
    total_pages: int


class ListUsersUseCase(UseCase[ListUsersInput, ListUsersOutput]):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, input_data: ListUsersInput) -> ListUsersOutput:
        users = await self.user_repository.index(
            input_data.page, input_data.page_size
        )
        total = len(users)

        total_pages = total // input_data.page_size
        if total % input_data.page_size != 0:
            total_pages += 1

        return ListUsersOutput(
            users=users, total=total, total_pages=total_pages
        )
