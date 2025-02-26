from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from app.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        pass  # pragma: no cover

    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[User]:
        pass  # pragma: no cover

    @abstractmethod
    async def find_by_id(self, user_id: UUID) -> Optional[User]:
        pass  # pragma: no cover

    @abstractmethod
    async def index(self, page: int, page_size: int) -> list[User]:
        pass  # pragma: no cover
