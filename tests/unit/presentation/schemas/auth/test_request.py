import pytest
from pydantic import ValidationError

from app.presentation.schemas.auth.request import LoginRequest
from tests.mocks.user import User

user_mock = User()


@pytest.mark.order(1)
def test_login_request_valid_data():
    login = LoginRequest(email=user_mock.email, password=user_mock.password)

    assert login.email == user_mock.email
    assert login.password == user_mock.password


@pytest.mark.order(2)
def test_login_request_min_password_length():
    with pytest.raises(ValidationError) as exc_info:
        LoginRequest(email=user_mock.email, password='Pass1!')

    assert 'String should have at least 8 characters' in str(exc_info.value)


@pytest.mark.order(3)
def test_login_request_invalid_email():
    with pytest.raises(ValidationError) as exc_info:
        LoginRequest(email='invalid_email', password=user_mock.password)

    assert '' in str(exc_info.value)
