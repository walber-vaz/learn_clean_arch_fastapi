from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    created_at: datetime | None = None


class UserDetailResponse(UserResponse):
    updated_at: datetime | None = None
