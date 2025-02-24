from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class User:
    name: str = 'Test User'
    email: str = 'email@email.com'
    password: str = '12345678'
    id: UUID = uuid4()
