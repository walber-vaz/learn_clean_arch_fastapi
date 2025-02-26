from pydantic import BaseModel, EmailStr, model_validator

MIN_NAME_LENGTH = 2
MIN_PASSWORD_LENGTH = 8


class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

    @model_validator(mode='after')
    def validate_data(self) -> 'UserCreateRequest':
        # Validar nome
        if not all(c.isalpha() or c.isspace() for c in self.name.strip()):
            raise ValueError('O nome deve conter apenas letras e espaços.')
        if len(self.name.strip()) < MIN_NAME_LENGTH:
            raise ValueError(
                f'O nome deve ter pelo menos {MIN_NAME_LENGTH} caracteres.'
            )
        self.name = ' '.join(word.capitalize() for word in self.name.split())

        # Validar senha
        if len(self.password) < MIN_PASSWORD_LENGTH:
            raise ValueError(
                f'A senha deve ter pelo menos {MIN_PASSWORD_LENGTH} caracteres.'  # noqa: E501
            )
        if not any(c.isupper() for c in self.password):
            raise ValueError(
                'A senha deve conter pelo menos uma letra maiúscula.'
            )
        if not any(c.isdigit() for c in self.password):
            raise ValueError('A senha deve conter pelo menos um número.')
        if not any(not c.isalnum() for c in self.password):
            raise ValueError(
                'A senha deve conter pelo menos um caractere especial (não alfanumérico).'  # noqa: E501
            )

        return self


class UserUpdateRequest(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None

    @model_validator(mode='after')
    def validate_data(self) -> 'UserUpdateRequest':
        # Validar nome se fornecido
        if self.name is not None:
            if not all(c.isalpha() or c.isspace() for c in self.name.strip()):
                raise ValueError('O nome deve conter apenas letras e espaços.')
            if len(self.name.strip()) < MIN_NAME_LENGTH:
                raise ValueError(
                    f'O nome deve ter pelo menos {MIN_NAME_LENGTH} caracteres.'
                )
            self.name = ' '.join(
                word.capitalize() for word in self.name.split()
            )

        # Validar senha se fornecida
        if self.password is not None:
            if len(self.password) < MIN_PASSWORD_LENGTH:
                raise ValueError(
                    f'A senha deve ter pelo menos {MIN_PASSWORD_LENGTH} caracteres.'  # noqa: E501
                )
            if not any(c.isupper() for c in self.password):
                raise ValueError(
                    'A senha deve conter pelo menos uma letra maiúscula.'
                )
            if not any(c.isdigit() for c in self.password):
                raise ValueError('A senha deve conter pelo menos um número.')
            if not any(not c.isalnum() for c in self.password):
                raise ValueError(
                    'A senha deve conter pelo menos um caractere especial (não alfanumérico).'  # noqa: E501
                )

        return self
