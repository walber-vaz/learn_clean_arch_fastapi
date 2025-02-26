from dataclasses import dataclass
from uuid import UUID, uuid4

from faker import Faker

faker = Faker('pt_BR')


@dataclass
class User:
    name: str = faker.name()
    email: str = faker.email()
    password: str = faker.password(
        length=8,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    )
    id: UUID = uuid4()
