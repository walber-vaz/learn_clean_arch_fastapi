from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import pytest
from faker import Faker
from freezegun import freeze_time

from app.infrastructure.security.jwt import (
    TokenPayload,
    create_access_token,
    decode_access_token,
)

fake = Faker('pt_BR')


@pytest.mark.order(1)
def test_create_access_token():
    sub = fake.uuid4()
    token = create_access_token(sub)

    assert token is not None
    assert isinstance(token, str)


@pytest.mark.order(2)
def test_decode_token_valid():
    sub = fake.uuid4()
    token = create_access_token(sub)

    decoded = decode_access_token(token)

    assert decoded is not None
    assert decoded.sub == sub
    assert decoded.exp is not None
    assert decoded.exp > datetime.now(ZoneInfo('America/Sao_Paulo'))
    assert isinstance(decoded.exp, datetime)
    assert isinstance(decoded, TokenPayload)


@pytest.mark.order(3)
def test_decode_token_expired():
    with freeze_time('2025-01-01 00:00:00'):
        sub = fake.uuid4()
        token = create_access_token(sub, timedelta(hours=1))

    with freeze_time('2025-01-01 01:00:01'):
        with pytest.raises(ValueError, match='Could not validate credentials'):
            decode_access_token(token)


@pytest.mark.order(4)
def test_decode_token_invalid():
    invalid_token = fake.sha256()

    with pytest.raises(ValueError, match='Could not validate credentials'):
        decode_access_token(invalid_token)
