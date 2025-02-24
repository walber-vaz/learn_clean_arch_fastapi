from typing import Generic, List, TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class PaginationParams(BaseModel):
    page: int = 1
    page_size: int = 10


class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int
    total_pages: int
