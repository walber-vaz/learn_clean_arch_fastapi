from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


def get_password_hash(password: str) -> str:
    """
    Gera um hash seguro a partir de uma senha em texto puro
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica se uma senha em texto puro corresponde ao hash armazenado
    """
    return pwd_context.verify(plain_password, hashed_password)
