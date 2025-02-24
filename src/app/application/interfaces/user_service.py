from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.entities.user import User


class UserService(ABC):
    @abstractmethod
    async def create_user(self, name: str, email: str, password: str) -> User:
        pass

    @abstractmethod
    async def get_user(self, user_id: UUID) -> User:
        pass

    @abstractmethod
    async def get_user_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    async def list_users(self) -> list[User]:
        pass
