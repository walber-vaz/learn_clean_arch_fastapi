from pydantic import BaseModel, EmailStr, field_validator

MIN_NAME_LENGTH = 2
MIN_PASSWORD_LENGTH = 8


class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

    @classmethod
    @field_validator('name')
    def validate_name(cls, value: str) -> str:
        value = value.strip()
        if not all(c.isalpha() or c.isspace() for c in value):
            raise ValueError('O nome deve conter apenas letras e espaços.')
        if len(value) < MIN_NAME_LENGTH:
            raise ValueError(
                f'O nome deve ter pelo menos {MIN_NAME_LENGTH} caracteres.'
            )
        return ' '.join(word.capitalize() for word in value.split())

    @classmethod
    @field_validator('password')
    def validate_password(cls, value: str) -> str:
        if len(value) < MIN_PASSWORD_LENGTH:
            raise ValueError(
                f'A senha deve ter pelo menos {MIN_PASSWORD_LENGTH} caracteres.'  # noqa: E501
            )

        if not any(c.isupper() for c in value):
            raise ValueError(
                'A senha deve conter pelo menos uma letra maiúscula.'
            )

        if not any(c.isdigit() for c in value):
            raise ValueError('A senha deve conter pelo menos um número.')

        if not any(not c.isalnum() for c in value):
            raise ValueError(
                'A senha deve conter pelo menos um caractere especial (não alfanumérico).'  # noqa: E501
            )

        return value


class UserUpdateRequest(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None

    @classmethod
    @field_validator('name')
    def validate_name(cls, value: str | None) -> str:
        if value is not None:
            value = value.strip()
            if not all(c.isalpha() or c.isspace() for c in value):
                raise ValueError('O nome deve conter apenas letras e espaços.')
            if len(value) < MIN_NAME_LENGTH:
                raise ValueError(
                    f'O nome deve ter pelo menos {MIN_NAME_LENGTH} caracteres.'
                )
            return ' '.join(word.capitalize() for word in value.split())
        return value

    @classmethod
    @field_validator('password')
    def validate_password(cls, value: str | None) -> str:
        if value is not None:
            if len(value) < MIN_PASSWORD_LENGTH:
                raise ValueError(
                    f'A senha deve ter pelo menos {MIN_PASSWORD_LENGTH} caracteres.'  # noqa: E501
                )

            if not any(c.isupper() for c in value):
                raise ValueError(
                    'A senha deve conter pelo menos uma letra maiúscula.'
                )

            if not any(c.isdigit() for c in value):
                raise ValueError('A senha deve conter pelo menos um número.')

            if not any(not c.isalnum() for c in value):
                raise ValueError(
                    'A senha deve conter pelo menos um caractere especial (não alfanumérico).'  # noqa: E501
                )

            return value
        return value
