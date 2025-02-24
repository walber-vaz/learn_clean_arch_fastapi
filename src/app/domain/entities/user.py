from datetime import datetime
from typing import Optional
from uuid import UUID
from zoneinfo import ZoneInfo

from sqlalchemy import text
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "tb_users"

    id: Optional[UUID] = Field(
        default=None,
        primary_key=True,
        index=True,
        unique=True,
        sa_column_kwargs={"server_default": text("gen_random_uuid()")},
    )
    name: str = Field(max_length=150, index=True, nullable=False)
    email: str = Field(max_length=150, index=True, nullable=False, unique=True)
    password: str = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(ZoneInfo("UTC")),
        nullable=False,
        sa_column_kwargs={"server_default": text("current_timestamp(6)")},
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(ZoneInfo("UTC")),
        nullable=False,
        sa_column_kwargs={"server_default": text("current_timestamp(6)")},
    )
