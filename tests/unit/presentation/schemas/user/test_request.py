import pytest
from pydantic import ValidationError

from app.presentation.schemas.user.request import (
    MIN_NAME_LENGTH,
    MIN_PASSWORD_LENGTH,
    UserCreateRequest,
    UserUpdateRequest,
)
from tests.mocks.user import User

user_mock = User()


@pytest.mark.order(1)
def test_user_create_request_valid_data():
    user = UserCreateRequest(
        name=user_mock.name, email=user_mock.email, password=user_mock.password
    )

    assert user.name == user_mock.name
    assert user.email == user_mock.email
    assert user.password == user_mock.password


@pytest.mark.order(2)
def test_user_create_request_invalid_name_characters():
    with pytest.raises(ValidationError) as exc_info:
        UserCreateRequest(
            name='John123',
            email=user_mock.email,
            password=user_mock.password,
        )
    assert 'O nome deve conter apenas letras e espaços.' in str(exc_info.value)


@pytest.mark.order(3)
def test_user_create_request_short_name():
    with pytest.raises(ValidationError) as exc_info:
        UserCreateRequest(
            name='J', email=user_mock.email, password=user_mock.password
        )
    assert f'O nome deve ter pelo menos {MIN_NAME_LENGTH} caracteres.' in str(
        exc_info.value
    )


@pytest.mark.order(4)
def test_user_create_request_short_password():
    with pytest.raises(ValidationError) as exc_info:
        UserCreateRequest(
            name=user_mock.name, email=user_mock.email, password='Pass1!'
        )
    assert (
        f'A senha deve ter pelo menos {MIN_PASSWORD_LENGTH} caracteres.'
        in str(exc_info.value)
    )


@pytest.mark.order(5)
def test_user_create_request_password_no_uppercase():
    with pytest.raises(ValidationError) as exc_info:
        UserCreateRequest(
            name=user_mock.name,
            email=user_mock.email,
            password='password1!',
        )
    assert 'A senha deve conter pelo menos uma letra maiúscula.' in str(
        exc_info.value
    )


@pytest.mark.order(6)
def test_user_create_request_password_no_digit():
    with pytest.raises(ValidationError) as exc_info:
        UserCreateRequest(
            name=user_mock.name, email=user_mock.email, password='Password!'
        )
    assert 'A senha deve conter pelo menos um número.' in str(exc_info.value)


@pytest.mark.order(7)
def test_user_create_request_password_no_special_character():
    with pytest.raises(ValidationError) as exc_info:
        UserCreateRequest(
            name=user_mock.name, email=user_mock.email, password='Password1'
        )
    assert (
        'A senha deve conter pelo menos um caractere especial (não alfanumérico).'  # noqa: E501
        in str(exc_info.value)
    )


@pytest.mark.order(8)
def test_user_update_request_empty():
    update_request = UserUpdateRequest()
    assert update_request.name is None
    assert update_request.email is None
    assert update_request.password is None


@pytest.mark.order(9)
def test_user_update_request_name_only():
    update_request = UserUpdateRequest(name=user_mock.name)
    assert update_request.name == user_mock.name
    assert update_request.email is None
    assert update_request.password is None


@pytest.mark.order(10)
def test_user_update_request_email_only():
    update_request = UserUpdateRequest(email=user_mock.email)
    assert update_request.name is None
    assert update_request.email == user_mock.email
    assert update_request.password is None


@pytest.mark.order(11)
def test_user_update_request_password_only():
    update_request = UserUpdateRequest(password=user_mock.password)
    assert update_request.name is None
    assert update_request.email is None
    assert update_request.password == user_mock.password


@pytest.mark.order(12)
def test_user_update_request_all_fields():
    update_request = UserUpdateRequest(
        name=user_mock.name, email=user_mock.email, password=user_mock.password
    )
    assert update_request.name == user_mock.name
    assert update_request.email == user_mock.email
    assert update_request.password == user_mock.password


@pytest.mark.order(13)
def test_user_update_request_invalid_name_characters():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdateRequest(name='John123')
    assert 'O nome deve conter apenas letras e espaços.' in str(exc_info.value)


@pytest.mark.order(14)
def test_user_update_request_short_name():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdateRequest(name='J')
    assert f'O nome deve ter pelo menos {MIN_NAME_LENGTH} caracteres.' in str(
        exc_info.value
    )


@pytest.mark.order(15)
def test_user_update_request_name_capitalization():
    update_request = UserUpdateRequest(name='john doe')
    assert update_request.name == 'John Doe'


@pytest.mark.order(16)
def test_user_update_request_invalid_email():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdateRequest(email='invalid_email')
    assert 'invalid_email' in str(exc_info.value)


@pytest.mark.order(17)
def test_user_update_request_short_password():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdateRequest(password='Pass1!')
    assert (
        f'A senha deve ter pelo menos {MIN_PASSWORD_LENGTH} caracteres.'
        in str(exc_info.value)
    )


@pytest.mark.order(18)
def test_user_update_request_password_no_uppercase():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdateRequest(password='password1!')
    assert 'A senha deve conter pelo menos uma letra maiúscula.' in str(
        exc_info.value
    )


@pytest.mark.order(19)
def test_user_update_request_password_no_digit():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdateRequest(password='Password!')
    assert 'A senha deve conter pelo menos um número.' in str(exc_info.value)


@pytest.mark.order(20)
def test_user_update_request_password_no_special_character():
    with pytest.raises(ValidationError) as exc_info:
        UserUpdateRequest(password='Password1')
    assert (
        'A senha deve conter pelo menos um caractere especial (não alfanumérico).'  # noqa: E501
        in str(exc_info.value)
    )
