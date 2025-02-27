from datetime import datetime, timedelta
from typing import Optional
from zoneinfo import ZoneInfo

from jwt import PyJWTError, decode, encode
from pydantic import BaseModel

from app.infrastructure.config.settings import settings


class TokenPayload(BaseModel):
    sub: str
    exp: datetime


def create_access_token(
    subject: str, expires_delta: Optional[timedelta] = None
) -> str:
    if expires_delta:
        expire = datetime.now(ZoneInfo('America/Sao_Paulo')) + expires_delta
    else:
        expire = datetime.now(ZoneInfo('America/Sao_Paulo')) + timedelta(
            minutes=settings.JWT_EXPIRATION
        )

    to_encode = {'sub': subject, 'exp': expire}
    encoded_jwt = encode(
        to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM
    )

    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = decode(
            token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        return token_data
    except PyJWTError:
        return ValueError('Could not validate credentials')
