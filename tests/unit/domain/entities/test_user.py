from app.domain.entities.user import User
from tests.mocks.user import User as MockUser


def test_user_entities_creation():
    user = User(
        name=MockUser.name, email=MockUser.email, password=MockUser.password
    )

    assert user.name == MockUser.name
    assert user.email == MockUser.email
    assert user.password == MockUser.password
    assert user.id is None
