from app.infrastructure.security.password import (
    get_password_hash,
    verify_password,
)
from tests.mocks.user import User as MockUser


def test_password_hash():
    password_hash = get_password_hash(MockUser.password)

    assert password_hash is not None
    assert password_hash != MockUser.password

    assert verify_password(MockUser.password, password_hash)

    assert not verify_password(MockUser.password + '1', password_hash)
